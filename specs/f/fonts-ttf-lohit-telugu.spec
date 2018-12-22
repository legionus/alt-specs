%define oldname lohit-telugu-fonts
%global fontname lohit-telugu
%global fontconf 65-0-%{fontname}.conf

Name:           fonts-ttf-lohit-telugu
Version:        2.5.3
Release:        alt1_6
Summary:        Free Telugu font

Group:          System/Fonts/True type
License:        OFL-1.0
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
Source1:       %{fontname}.metainfo.xml
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Obsoletes: lohit-fonts-common < %{version}-%{release}
Patch1: bug-1105878.patch
Source44: import.info


%description
This package provides a free Telugu truetype/opentype font.

%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-0-lohit-telugu.conf
%patch1 -p1 -b .1-Conjunct-character-rendering-issue


%build
make %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
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

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README ChangeLog.old
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_5
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_4
- update to new release by fcimport

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_2
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_1
- update to new release by fcimport

* Sat Nov 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1_3
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1_2
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2
- update to new release by fcimport

* Mon Oct 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_1
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.5-alt3_14
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.5-alt2_14
- bugfix release by fcimport

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.5-alt1_14
- initial release by fcimport

