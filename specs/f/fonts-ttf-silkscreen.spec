%define oldname silkscreen-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname silkscreen
%global fontconf 60-%{fontname}

%global common_desc \
Silkscreen is a four member type family for your Web graphics created by Jason \
Kottke. Silkscreen is best used in places where extremely small graphical \
display type is needed. The primary use is for navigational items (nav bars, \
menus, etc), but it works well wherever small type is needed. In order to \
preserve the proper spacing and letterforms, Silkscreen should be used at 8pt. \
multiples (8pt., 16pt., 24pt., etc.) with anti-aliasing turned off. \

Name:		fonts-ttf-silkscreen
Summary: 	Silkscreen four member type family
Version:	1.0
Release:	alt3_16
# License attribution confirmed by author and Open Font Library
# http://openfontlibrary.org/media/files/jkottke/218
License:	OFL
Group:		System/Fonts/True type
Source0:	http://www.kottke.org/plus/type/silkscreen/download/silkscreen.tar.gz
Source1:	%{oldname}-fontconfig.conf
Source2:	%{oldname}-expanded-fontconfig.conf
Source3:	%{fontname}.metainfo.xml
Source4:	%{fontname}-expanded.metainfo.xml
URL:		http://www.kottke.org/plus/type/silkscreen/
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	%{name}-common = %{version}-%{release}
Source44: import.info

%description
%common_desc

%package -n fonts-ttf-silkscreen-common
Summary:	Common files for Silkscreen fonts (documentation...)
Group:		System/Fonts/True type

%description -n fonts-ttf-silkscreen-common
%common_desc

This package consists of files used by other Silkscreen packages.

%package -n fonts-ttf-silkscreen-expanded
Summary:	Expanded Silkscreen font family
Group:		System/Fonts/True type
Requires:	%{name}-common = %{version}-%{release}

%description -n fonts-ttf-silkscreen-expanded
%common_desc

This font family has a slightly expanded spacing between the letters in 
comparison to the normal Silkscreen font family.

%files -n fonts-ttf-silkscreen-expanded
%{_fontconfig_templatedir}/%{fontconf}-expanded.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-expanded.conf
%{_fontbasedir}/*/%{_fontstem}/slkscre*.ttf
%{_datadir}/appdata/%{fontname}-expanded.metainfo.xml

%prep
%setup -q -c -n %{oldname}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-expanded.conf

for fontconf in %{fontconf}.conf %{fontconf}-expanded.conf ; do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-expanded.metainfo.xml
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
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/slkscr.ttf
%{_fontbasedir}/*/%{_fontstem}/slkscrb.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%files -n fonts-ttf-silkscreen-common
%doc readme.txt
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_16
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_11
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- initial release by fcimport

