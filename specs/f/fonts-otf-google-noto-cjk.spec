Group: System/Fonts/True type
%define oldname google-noto-cjk-fonts
%define fedora 26
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit0 32a5844539f2e348ed36b44e990f9b06d7fb89fe
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global fontname google-noto-cjk
%global fontconf 66-%{fontname}


Name:           fonts-otf-google-noto-cjk
Version:        20170602
Release:        alt1_2
Summary:        Google Noto Sans CJK Fonts

License:        OFL
URL:            https://github.com/googlei18n/noto-cjk
Source0:        https://github.com/googlei18n/noto-cjk/archive/%{commit0}.tar.gz#/noto-cjk-%{shortcommit0}.tar.gz
Source1:        %{fontconf}-simplified-chinese.conf
Source2:        %{fontconf}-traditional-chinese.conf
Source3:        %{fontconf}-japanese.conf
Source4:        %{fontconf}-korean.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%if 0%{?fedora}

Obsoletes:      google-noto-sans-cjk-fonts < 20150617
Provides:       google-noto-sans-cjk-fonts = 20150617

# noto cjk replace
%define notocjkrep(:)\
%define pname %(echo %{*} | tr "A-Z " "a-z-")\
Obsoletes:      google-noto-%{pname}-fonts < 20150617\
Provides:       google-noto-%{pname}-fonts = 20150617\
Obsoletes:      google-noto-cjk-%{pname}-fonts < %{version}-%{release}\
Provides:       google-noto-cjk-%{pname}-fonts = %{version}-%{release}\


%notocjkrep Sans Simplified Chinese
%notocjkrep Sans Traditional Chinese
%notocjkrep Sans Japanese
%notocjkrep Sans Korean

%endif
Source44: import.info


%description
Noto Sans CJK is a sans serif typeface designed as an intermediate style 
between the modern and traditional.
It is intended to be a multi-purpose digital font for user interface designs, 
digital content, reading on laptops, mobile devices, and electronic books.
Noto Sans CJK comprehensively covers Simplified Chinese, Traditional Chinese, 
Japanese, and Korean in a unified font family.
It supports regional variants of ideographic characters for each of 
the four languages.
In addition, it supports Japanese kana, vertical forms, and variant characters 
(itaiji); it supports Korean hangeul a.. both contemporary and archaic.


%prep
%setup -q -n noto-cjk-%{commit0}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p NotoSansCJK-*.ttc %{buildroot}%{_fontdir}
install -m 0644 -p NotoSerifCJK-*.ttc %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
            %{buildroot}%{_fontconfig_confdir}

for f in simplified-chinese traditional-chinese \
    japanese korean;
do
    install -m 0644 -p %{fontconf}-$f.conf \
                %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-$f.conf

    ln -s %{_fontconfig_templatedir}/%{fontconf}-$f.conf \
         %{buildroot}%{_fontconfig_confdir}/%{fontconf}-$f.conf
done
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi


%files
%{_fontconfig_templatedir}/*.conf
%config(noreplace) %{_fontconfig_confdir}/*.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansCJK-*.ttc
%{_fontbasedir}/*/%{_fontstem}/NotoSerifCJK-*.ttc
%doc NEWS HISTORY README.formats README.third_party
%doc LICENSE


%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 20170602-alt1_2
- update to new release by fcimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_5
- converted for ALT Linux by srpmconvert tools

