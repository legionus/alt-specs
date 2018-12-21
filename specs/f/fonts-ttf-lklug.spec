%define oldname lklug-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname lklug
%global cvsdate 20090803
%global fontconf 65-%{fontname}.conf

Name:	fonts-ttf-lklug
# Do not trust font metadata versionning unless you've checked upstream does
# update versions on file changes. When in doubt use the timestamp of the most
# recent file as version.
Version:	0.6
Release:	alt3_16.%{cvsdate}cvs
Summary:	Fonts for Sinhala language
Group:	System/Fonts/True type
License:	GPLv2
URL:	http://sinhala.sourceforge.net/
# cvs snapshot created with following steps
#cvs -z3 -d:pserver:anonymous@sinhala.cvs.sourceforge.net:/cvsroot/sinhala co -P sinhala/fonts
#cd sinhala/fonts/
#tar -czf lklug-%%{cvsdate}.tar.gz convert.ff COPYING  CREDITS lklug.sfd Makefile README.fonts

Source:	lklug-%{cvsdate}.tar.gz
Source1:	%{fontconf}
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel fontforge libfontforge
Source44: import.info

%description
The lklug-fonts package contains fonts for the display of
Sinhala. The original font for TeX/LaTeX is developed by Yannis 
Haralambous and are in GPL. OTF tables are added by Anuradha 
Ratnaweera and Harshani Devadithya.

%prep
%setup -n %{oldname}-%{version} -q -c

%build
make

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

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
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc CREDITS COPYING README.fonts 
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_16.20090803cvs
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_12.20090803cvs
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_11.20090803cvs
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_9.20090803cvs
- update to new release by fcimport

* Sat Nov 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_8.20090803cvs
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_7.20090803cvs
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_6.20090803cvs
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_6.20090803cvs
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_5.20090803cvs
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_5.20090803cvs
- initial release by fcimport

