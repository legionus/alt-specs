# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname saab-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname saab
%global fontconf 67-%{fontname}.conf

Name:        fonts-otf-saab
Version:     0.91
Release:     alt3_15
Summary:     Free Punjabi Unicode OpenType Font

Group:       System/Fonts/True type

License:     GPLv2+ with exceptions
URL:         http://guca.sourceforge.net/typography/fonts/saab/
Source0:     http://downloads.sf.net/guca/saab.0.91.zip
Source1:     %{oldname}-fontconfig.conf
#Font file itself does not add exception text, so add it manually
#from http://guca.sourceforge.net/typography/fonts/saab/
Source2:     License_font_exception.txt
BuildArch:   noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description 
This package provides a free OpenType Punjabi (Gurmukhi) font. 
Developed by Bhupinder Singh


%prep
%setup -n %{oldname}-%{version} -q -c

%build
echo "Nothing to do in Build."

%install
install -m 0644 -p %{SOURCE2} .
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Saab.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
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
%{_fontbasedir}/*/%{_fontstem}/Saab.otf
%doc License_font_exception.txt

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_15
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_9
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.91-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.91-alt2_5
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_5
- initial release by fcimport

