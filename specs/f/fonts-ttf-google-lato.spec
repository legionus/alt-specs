# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname lato-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname lato
%global fontconf 61-%{fontname}.conf

Name:           fonts-ttf-google-lato
Version:        2.015
Release:        alt1_4
Summary:        A sanserif typeface family

Group:          System/Fonts/True type
License:        OFL-1.0
URL:            http://www.latofonts.com/
# Fonts retrieved 2015-08-07 from http://www.latofonts.com/download/Lato2OFL.zip
Source0:        %{oldname}-%{version}.zip
Source1:        %{oldname}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Provides:       google-lato-fonts = %{version}-%{release}
Obsoletes:      google-lato-fonts < 1.014-1
Source44: import.info

%description
Lato is a sanserif typeface family designed in the Summer 2010 by Warsaw-based
designer A.ukasz Dziedzic ("Lato" means "Summer" in Polish). In December 2010 the
Lato family was published under the open-source Open Font License by his foundry
tyPoland, with support from Google.

When working on Lato, A.ukasz tried to carefully balance some potentially
conflicting priorities. He wanted to create a typeface that would seem quite
"transparent" when used in body text but would display some original treats when
used in larger sizes. He used classical proportions (particularly visible in the
uppercase) to give the letterforms familiar harmony and elegance. At the same
time, he created a sleek sanserif look, which makes evident the fact that Lato
was designed in 2010 - even though it does not follow any current trend.

The semi-rounded details of the letters give Lato a feeling of warmth, while the
strong structure provides stability and seriousness. "Male and female, serious
but friendly. With the feeling of the Summer," says A.ukasz.

Lato consists of nine weights (plus corresponding italics), including a
beautiful hairline style. It covers 2300+ glyphs per style and supports 100+
Latin-based languages, 50+ Cyrillic-based languages as well as Greek and IPA
phonetics.


%prep
%setup -n %{oldname}-%{version} -q -c

# Fix wrong end-of-lines encoding
sed "s/\r//" Lato2OFL/OFL.txt > Lato2OFL/OFL.txt.new
touch -r Lato2OFL/OFL.txt Lato2OFL/OFL.txt.new
mv Lato2OFL/OFL.txt.new Lato2OFL/OFL.txt

# Fix permissions
chmod 0644 Lato2OFL/{OFL.txt,README.txt}


%build


%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p Lato2OFL/*.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d $RPM_BUILD_ROOT%{_fontconfig_templatedir} $RPM_BUILD_ROOT%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} $RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

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
%doc Lato2OFL/README.txt
%doc Lato2OFL/OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.015-alt1_4
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.010-alt1_2
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.007-alt1_2
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.014-alt1_3
- update to new release by fcimport

* Mon Nov 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.014-alt1_2
- fc import

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.011-alt3_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.011-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.011-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.011-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.011-alt1_2
- initial release by fcimport

