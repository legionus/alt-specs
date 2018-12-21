Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname khmeros-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 5.0
%global fontname khmeros
%global archivename All_KhmerOS_%{version}

%global fontconf 65-0-%{fontname}

%global common_desc \
The Khmer OS fonts include Khmer and Latin alphabets, and they have equivalent \
sizes for Khmer and English alphabets, so that when texts mix both it is not \
necessary to have different point sizes for the text in each language. \
\
They were created by Danh Hong of the Cambodian Open Institute.


Name:           fonts-ttf-khmeros
Version:        5.0
Release:        alt3_25
Summary:        Khmer font set created by Danh Hong of the Cambodian Open Institute

License:        LGPLv2+
URL:            http://www.khmeros.info/en/fonts
Source0:        http://downloads.sourceforge.net/khmer/%{archivename}.zip
Source1:        65-0-khmeros-battambang.conf
Source2:        65-0-khmeros-bokor.conf
Source3:        65-0-khmeros-handwritten.conf
Source4:        65-0-khmeros-base.conf
Source5:        65-0-khmeros-metal-chrieng.conf
Source6:        65-0-khmeros-muol.conf
Source7:        65-0-khmeros-siemreap.conf
Source8:        License.txt
Source9:        %{fontname}-base.metainfo.xml
Source10:        %{fontname}-battambang.metainfo.xml
Source11:        %{fontname}-bokor.metainfo.xml
Source12:        %{fontname}-handwritten.metainfo.xml
Source13:        %{fontname}-metal-chrieng.metainfo.xml
Source14:        %{fontname}-muol.metainfo.xml
Source15:        %{fontname}-siemreap.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc


%package -n fonts-ttf-khmeros-common
Group: System/Fonts/True type
Summary:        Common files of %{oldname}

%description -n fonts-ttf-khmeros-common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-khmeros-base
Group: System/Fonts/True type
Summary:        Base KhmerOS font
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-khmeros-base
%common_desc

Base KhmerOS fonts.

%files -n fonts-ttf-khmeros-base
%{_fontconfig_templatedir}/65-0-khmeros-base.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-base.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/KhmerOS.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_content.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_sys.ttf
%{_datadir}/appdata/%{fontname}-base.metainfo.xml


%package -n fonts-ttf-khmeros-battambang
Group: System/Fonts/True type
Summary:        Battambang font
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-khmeros-battambang
%common_desc

Battambang font.

%files -n fonts-ttf-khmeros-battambang
%{_fontconfig_templatedir}/65-0-khmeros-battambang.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-battambang.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_battambang.ttf
%{_datadir}/appdata/%{fontname}-battambang.metainfo.xml


%package -n fonts-ttf-khmeros-bokor
Group: System/Fonts/True type
Summary:        Bokor font
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-khmeros-bokor
%common_desc

Bokor font.

%files -n fonts-ttf-khmeros-bokor
%{_fontconfig_templatedir}/65-0-khmeros-bokor.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-bokor.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_bokor.ttf
%{_datadir}/appdata/%{fontname}-bokor.metainfo.xml

%package -n fonts-ttf-khmeros-handwritten
Group: System/Fonts/True type
Summary:        Freehand and fasthand fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-khmeros-handwritten
%common_desc

Freehand and fasthand - handwritten fonts.

%files -n fonts-ttf-khmeros-handwritten
%{_fontconfig_templatedir}/65-0-khmeros-handwritten.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-handwritten.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_freehand.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_fasthand.ttf
%{_datadir}/appdata/%{fontname}-handwritten.metainfo.xml

%package -n fonts-ttf-khmeros-metal-chrieng
Group: System/Fonts/True type
Summary:        Metal Chrieng font
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-khmeros-metal-chrieng
%common_desc

Metal Chrieng font.

%files -n fonts-ttf-khmeros-metal-chrieng
%{_fontconfig_templatedir}/65-0-khmeros-metal-chrieng.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-metal-chrieng.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_metalchrieng.ttf
%{_datadir}/appdata/%{fontname}-metal-chrieng.metainfo.xml

%package -n fonts-ttf-khmeros-muol
Group: System/Fonts/True type
Summary:        Muol fonts - normal, light and Pali
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-khmeros-muol
%common_desc

Muol fonts - normal, light and Pali.

%files -n fonts-ttf-khmeros-muol
%{_fontconfig_templatedir}/65-0-khmeros-muol.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-muol.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_muol.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_muollight.ttf
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_muolpali.ttf
%{_datadir}/appdata/%{fontname}-muol.metainfo.xml

%package -n fonts-ttf-khmeros-siemreap
Group: System/Fonts/True type
Summary:        Siemreap font
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-khmeros-siemreap
%common_desc

Siemreap font.

%files -n fonts-ttf-khmeros-siemreap
%{_fontconfig_templatedir}/65-0-khmeros-siemreap.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-khmeros-siemreap.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/KhmerOS_siemreap.ttf
%{_datadir}/appdata/%{fontname}-siemreap.metainfo.xml


%prep
%setup -q -n %{archivename}

install -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .
install -p %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} .


%build
#nothing

%install
# get rid of the white space (' ')
mv 'KhmerOS .ttf' KhmerOS.ttf

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

for conffile in *.conf ; do
install -m 0644 -p $conffile %{buildroot}%{_fontconfig_templatedir}/${conffile}
ln -s %{_fontconfig_templatedir}/$conffile \
      %{buildroot}%{_fontconfig_confdir}/$conffile
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-base.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-battambang.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-bokor.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-handwritten.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-metal-chrieng.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-muol.metainfo.xml
install -Dm 0644 -p %{SOURCE15} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-siemreap.metainfo.xml
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


%files -n fonts-ttf-khmeros-common
%doc --no-dereference License.txt


%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_25
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_23
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_19
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_18
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_16
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_15
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_14
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_13
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt3_12
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.0-alt2_12
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 5.0-alt2_11
- rebuild with new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_11
- initial release by fcimport

