# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname nhn-nanum-gothic-coding-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%global fontname nhn-nanum-gothic-coding
%global fontconf 65-3-%{fontname}.conf

%global archivename NanumGothicCoding-2.0.zip

Name:		fonts-ttf-nhn-nanum-gothic-coding
Version:	2.000
Release:	alt1_8
Summary:	Nanum Gothic Coding family of Korean TrueType fonts

Group:		System/Fonts/True type
License:	OFL-1.0
URL:		http://dev.naver.com/projects/nanumfont/
# NanumGothic_Coding has a mirror redirector for its downloads
# You can get this zip archive by following a link from:
# http://dev.naver.com/projects/nanumfont/download/note/214
Source0:	%{archivename}
Source1:	%{oldname}-fontconfig.conf

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
Nanum Gothic Coding fonts are set of Gothic Korean font faces suitable
for source code editing, designed by Sandoll Communication and
published by NHN Corporation.

%prep
export LANG=en_US.ISO8859-1
%setup -n %{oldname}-%{version} -q -c
for i in *.ttf; do
  case $i in
    *-Bold.ttf)
      mv $i NanumGothic_Coding_Bold.ttf
      ;;
    *) 
      mv $i NanumGothic_Coding.ttf
  esac
done


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

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
%{_fontbasedir}/*/%{_fontstem}/*.ttf


%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_2
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_1
- new version

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.500-alt3_4
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.500-alt3_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.500-alt3_2
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.500-alt2_2
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.500-alt2_1
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.500-alt1_1
- initial release by fcimport

