Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname jomolhari-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global	fontname jomolhari
%global fontconf 65-0-%{fontname}.conf

Name:		fonts-ttf-jomolhari
Version:	0.003
Release:	alt3_23
Summary:	Jomolhari a Bhutanese style font for Tibetan and Dzongkha

License:	OFL
# Looks like currently following URL is gone now. Maybe temporary issue
#URL:		http://chris.fynn.googlepages.com/jomolhari
# Try following URL for this package
#URL:           https://sites.google.com/site/chrisfynn2/home/fonts/jomolhari
Source0:	http://chris.fynn.googlepages.com/jomolhari-alpha003c.zip
Source1:        %{oldname}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
Jomolhari is an TrueType OpenType Bhutanese style font for Dzongkha and
Tibetan text. It is based on Bhutanese manuscript examples, supports the
Unicode and the Chinese encoding for Tibetan.
The font supports the standard combinations used in most texts.

%prep
%setup -n %{oldname}-%{version} -q -c

%build
# Empty build section

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

for i in FONTLOG.txt OFL-FAQ.txt OFL.txt
do
	tr -d '\r' < $i > ${i}.tmp
	mv -f ${i}.tmp $i
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
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
%{_fontconfig_templatedir}/65-0-%{fontname}.conf
%config(noreplace) %{_fontconfig_confdir}/65-0-%{fontname}.conf
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc FONTLOG.txt OFL-FAQ.txt OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_23
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_19
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_18
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_16
- update to new release by fcimport

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_15
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_12
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_11
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_11
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_10
- rebuild with new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_10
- initial release by fcimport

