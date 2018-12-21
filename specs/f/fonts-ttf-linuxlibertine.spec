Group: System/Fonts/True type
%define oldname linux-libertine-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname            linux-libertine
%global prio_libertine      60
%global prio_biolinum       61
%global fontconf_libertine  %{prio_libertine}-%{fontname}-libertine.conf
%global fontconf_biolinum   %{prio_biolinum}-%{fontname}-biolinum.conf
%global fontconf_metrics    29-%{fontname}-metrics-alias.conf
%global archivename         LinLibertine
%global posttag             2012_07_02

%define common_desc                                                     \
The Linux Libertine Open Fonts are a TrueType font family for practical \
use in documents.  They were created to provide a free alternative to   \
proprietary standard fonts.

Name:           fonts-ttf-linuxlibertine
Version:        5.3.0
Release:        alt1_12.%{posttag}
Summary:        Linux Libertine Open Fonts

License:        GPLv2+ with exceptions or OFL
URL:            http://linuxlibertine.sf.net
Source0:        http://download.sourceforge.net/sourceforge/linuxlibertine/LinLibertineOTF_%{version}_%{posttag}.tgz
Source1:        %{oldname}-libertine-fontconfig.conf
Source2:        %{oldname}-biolinum-fontconfig.conf
Source3:        %{oldname}-libertine-metrics-alias-fontconfig.conf
Source4:        libertine.metainfo.xml
Source5:        biolinum.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
#BuildRequires:  fontforge
Requires:       fonts-ttf-linuxlibertine-common = %{version}-%{release}
Source44: import.info

%description
%common_desc

This package contains Serif fonts.

%package -n fonts-ttf-linuxlibertine-biolinum
Group: System/Fonts/True type
Summary:        Sans-serif fonts from Linux Libertine Open Fonts
Requires:       fonts-ttf-linuxlibertine-common = %{version}-%{release}

%description -n fonts-ttf-linuxlibertine-biolinum
%common_desc

This package contains Sans fonts.

%package -n fonts-ttf-linuxlibertine-common
Group: System/Fonts/True type
Summary:        Common files for Linux Libertine Open Fonts

%description -n fonts-ttf-linuxlibertine-common
%common_desc

This package consists of files used by other %{oldname} packages.

%prep
%setup -n %{oldname}-%{version} -q -c
sed -i -e 's/\r//' OFL-1.1.txt

%build
#for i in $(find -name '*.sfd'); do
#  (cd scripts;
#   ./bailly-2.sh "../$i" ttf
#  )
#done
#mv scripts/*.ttf .

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf_libertine}
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf_biolinum}
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf_metrics}

for fconf in %{fontconf_libertine} %{fontconf_metrics} %{fontconf_biolinum}; do
    ln -s %{_fontconfig_templatedir}/$fconf \
          %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/libertine.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/biolinum.metainfo.xml
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

%files -n fonts-ttf-linuxlibertine-common
%doc --no-dereference GPL.txt LICENCE.txt OFL-1.1.txt
%doc Bugs.txt ChangeLog.txt Readme-TEX.txt README

%files
%{_fontconfig_templatedir}/%{fontconf_libertine}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf_libertine}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/LinLibertine*.otf
%{_datadir}/appdata/libertine.metainfo.xml

%{_fontconfig_templatedir}/%{fontconf_metrics}
%{_fontconfig_confdir}/%{fontconf_metrics}

%files -n fonts-ttf-linuxlibertine-biolinum
%{_fontconfig_templatedir}/%{fontconf_biolinum}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf_biolinum}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/LinBiolinum*.otf
%{_datadir}/appdata/biolinum.metainfo.xml

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 5.3.0-alt1_12.2012_07_02
- update to new release by fcimport

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 5.3.0-alt1_10.2012_07_02
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 5.3.0-alt1_5.2012_07_02
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 5.3.0-alt1_3.2012_07_02
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 5.3.0-alt1_2.2012_07_02
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.7.5-alt2_2.2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.7.5-alt1_2.2
- update to new release by fcimport

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 4.7.5-alt1_1.2
- added provides/obsoletes for short names

* Thu Dec 10 2009 Vitaly Lipatov <lav@altlinux.ru> 4.4.1-alt1
- new version 4.4.1 (with rpmrb script)

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.7.9-alt1
- new version (2.7.9)

* Fri Sep 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.6.9-alt1
- new version 2.6.9 (with rpmrb script)

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 2.5.9-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Sun May 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.5.9-alt1
- initial build for ALT Linux Sisyphus
