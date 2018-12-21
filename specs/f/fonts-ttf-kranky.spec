Group: System/Fonts/True type
%define oldname kranky-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname kranky
%global fontconf 61-%{fontname}-fonts.conf
%global checkout 716ff965e2b0hg


Name:          fonts-ttf-kranky
Version:       1.00
Release:       alt1_8.%{checkout}
Summary:       Kranky fonts
License:       ASL 2.0
URL:           http://www.google.com/fonts/specimen/Kranky
Source0:       https://googlefontdirectory.googlecode.com/hg/apache/kranky/Kranky.ttf
Source1:       https://googlefontdirectory.googlecode.com/hg/apache/kranky/LICENSE.txt
Source10:      %{fontconf}
BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge libfontforge
BuildRequires: ttname
Source44: import.info

%description
Get happy? No! Get Kranky! Another hand-crafted, fun-filled font guaranteed to
put a smile on your face. So grab it now and put on a big old I-got-it-for-free
grin. But before your face gets stuck like that be sure to check out all the
other inappropriately named fonts by Squid.


%prep
cp -p %{SOURCE0} %{SOURCE1} .


%build
ttname --copyright="Font Diner, Inc DBA Sideshow (diner@fontdiner.com)" --license="$(cat LICENSE.txt)" --license-url="https://www.apache.org/licenses/LICENSE-2.0" *.ttf || exit 0


%install

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc LICENSE.txt


%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_8.716ff965e2b0hg
- update to new release by fcimport

* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_5.716ff965e2b0hg
- new version
