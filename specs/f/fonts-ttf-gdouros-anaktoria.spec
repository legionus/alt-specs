Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gdouros-anaktoria-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname gdouros-anaktoria
%global fontconf 65-%{fontname}.conf

Name:           fonts-ttf-gdouros-anaktoria
Version:        8.01
Release:        alt1_1
Summary:        A font based on "Grecs du roi" and the "First Folio Edition of Shakespeare"
License:        ALT-Public-Domain
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Textfonts.zip
Source1:        %{oldname}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:     gdouros-textfonts-doc
Source44: import.info

%description
Greek letters are based on "Grecs du roi" designed by Claude Garamond (1480-
1561) between 1541 and 1544, commissioned by king Francis I of France, for the
exclusive use by the Imprimerie Nationale in Paris. Mindaugas Strockis prepared
a modern version of "Grecs du roi" in 2001.

Latin letters have been digitized directly out of the titles and front pages of
the 1623 "First Folio Edition of Shakespeare". Scott Mann and Peter Guither
prepared a modern version of the font for "The Illinois Shakespeare Festival"
in 1995.

The font covers the Windows Glyph List, IPA Extensions, Greek Extended, Ancient
Greek Numbers, Byzantine and Ancient Greek Musical Notation, various
typographic extras and several Open Type features (Case-Sensitive Forms, Small
Capitals, Subscript, Superscript, Numerators, Denominators, Fractions, Old
Style Figures, Historical Forms, Stylistic Alternates, Ligatures).

It was created by George Douros.

%prep
%setup -n %{oldname}-%{version} -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/Anaktoria.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml
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

%check
appstream-util validate-relax --nonet \
      %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml


%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Anaktoria.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 8.01-alt1_1
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 7.17-alt1_3
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 6.31-alt1_1
- update to new release by fcimport

* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 6.00-alt1_1
- new version

