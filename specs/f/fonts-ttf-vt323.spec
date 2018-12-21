Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: python
# END SourceDeps(oneline)
%define oldname vt323-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname vt323
%global fontconf 61-%{fontname}-fonts.conf
%global alphatag 20140916hg


Name:          fonts-ttf-vt323
Version:       1.002
Release:       alt1_0.4.%{alphatag}
Summary:       VT323 font by Peter Hull
License:       OFL
URL:           https://www.google.com/fonts/specimen/VT323
Source0:       https://googlefontdirectory.googlecode.com/hg/ofl/vt323/src/VT323-Regular-TTF.sfd
Source1:       https://googlefontdirectory.googlecode.com/hg/ofl/vt323/OFL.txt
Source10:      %{fontconf}
BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge libfontforge
BuildRequires: ttname
Source44: import.info

%description
This font was created from the glyphs of the DEC VT320 text terminal.


%prep
%setup -n %{oldname}-%{version} -qTc
cp -p %{SOURCE0} %{SOURCE1} .
# Correct end of line encoding for OFL.txt
sed -i 's/\r$//' OFL.txt


%build
fontforge -lang=ff -script "-" *.sfd <<_EOF
i = 1
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5)
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
_EOF
ttname --copyright="$(head -n1 OFL.txt)" --license="$(cat OFL.txt)" --license-url="http://scripts.sil.org/OFL" *.ttf || exit 0

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
%doc OFL.txt *.pdf


%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1_0.4.20140916hg
- update to new release by fcimport

* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1_0.2.20140916hg
- new version

