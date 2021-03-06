Group: System/Fonts/True type
%define oldname serafettin-cartoon-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name serafettin-cartoon-fonts
%define version 0.6
%define fontname serafettin-cartoon
%define fontconf 66-%{fontname}.conf
%define archivename %{oldname}-%{version}

Name:          fonts-ttf-serafettin-cartoon
Version:       0.6
Release:       alt3_12
Summary:       Sans-serif Cartoon Fonts
License:       GPLv2+
URL:           http://serafettin.sourceforge.net/
Source0:       http://downloads.sourceforge.net/serafettin/%{archivename}.tar.xz
Source1:       %{fontname}.metainfo.xml
Source2:       %{fontname}-condensed.metainfo.xml

BuildArch:     noarch

BuildRequires: fontforge libfontforge
BuildRequires: fontpackages-devel
Source44: import.info


%description
Serafettin aims to be a collection of free Latin fonts for daily usage.
Currently it contains a free cartoon sans-serif font. It is based on Thukkaram 
Gopalrao's TSCu_Comic of tamillinux project. 

%prep
%setup -q -n %{archivename}


%build
export FONTFORGE_VERBOSE=1
make %{?_smp_flags}


%install
DESTDIR=%{buildroot} make install

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontname}.conf \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml
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
%doc ChangeLog.txt COPYING.txt FONTLOG.txt README.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml
%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_12
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_2
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_2
- initial release by fcimport

