Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname drehatlas-widelands-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname drehatlas-widelands
%global fontconf 61-%{fontname}.conf
%global metapkgver 2010-02-06

# This is a highly-stylized titling font, so picking an ideal substitute with
# fontconfig is pointless

Name:		fonts-otf-drehatlas-widelands
Version:	1.0.3.1
Release:	alt3_17
Summary:	A Latin typeface inspired by feudal calligraphy
License:	OFL-1.0
URL:		http://www.drehatlas.de/
Source0:	http://downloads.sourceforge.net/project/drehatlas-fonts/Font-Packages/COMPLETE/drehatlas-fonts-%{metapkgver}.zip
Source1:	%{fontconf}
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel fontforge libfontforge
Source44: import.info

%description
This font was created by Peter Schwanemann as a logo for the Widelands project,
but has since been enhanced.  The font is decorative and not really usable for
real texts, but it looks nice for logos, banners or similar stuff.  All normal
latin glyphs and arabic numbers are included and usable.

%prep
%setup -n %{oldname}-%{version} -q -c %{oldname}-%{version}
cd drehatlas-fonts-%{metapkgver}/Widelands-%{version}
# Wrap the license file at 80 chars
fold -s LICENSE > LICENSE.new
touch -r LICENSE LICENSE.new
mv LICENSE.new LICENSE

%build

%install
cd drehatlas-fonts-%{metapkgver}/Widelands-%{version}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc drehatlas-fonts-%{metapkgver}/Widelands-%{version}/LICENSE drehatlas-fonts-%{metapkgver}/Widelands-%{version}/FONTLOG

%changelog
* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_17
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_14
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_13
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt2_6
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3.1-alt1_6
- initial release by fcimport

