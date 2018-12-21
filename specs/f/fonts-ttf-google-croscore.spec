Group: Graphical desktop/Other
%define oldname google-croscore-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname google-croscore
%global fontconf62 62-%{fontname}
%global fontconf30 30-0-%{fontname}

%global common_desc \
This package contains a collections of fonts that offers improved on-screen \
readability characteristics and the pan-European WGL character set and solves \
the needs of developers looking for width-compatible fonts to address document \
portability across platforms.


Name:           fonts-ttf-google-croscore
Version:        1.31.0
Release:        alt1_2
Summary:        The width-compatible fonts for improved on-screen readability

License:        ASL 2.0
#URL:            
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/croscorefonts-%{version}.tar.bz2

Source1:        62-%{fontname}-arimo-fontconfig.conf
Source2:        62-%{fontname}-cousine-fontconfig.conf
Source3:        62-%{fontname}-tinos-fontconfig.conf
Source4:        30-0-%{fontname}-arimo-fontconfig.conf
Source5:        30-0-%{fontname}-cousine-fontconfig.conf
Source6:        30-0-%{fontname}-tinos-fontconfig.conf

# Upstream has not provided license text in their tarball release
# Add ASL2.0 license text in LICENSE-2.0.txt file
Source8:        LICENSE-2.0.txt

# metainfo files for gnome-software
Source9:        %{fontname}-arimo.metainfo.xml
Source10:        %{fontname}-cousine.metainfo.xml
Source11:        %{fontname}-tinos.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc


%package -n fonts-ttf-google-croscore-common
Group: System/Fonts/True type
Summary:        Common files of %{oldname}

# As upstream stopped distributing SymbolNeu font, let's obsolete this subpackage.
Obsoletes:      google-croscore-symbolneu-fonts < 1.31.0-1

%description -n fonts-ttf-google-croscore-common
This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-google-croscore-arimo
Group: System/Fonts/True type
Summary:       The croscore Arimo family fonts 
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-google-croscore-arimo
%common_desc
Arimo was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Arial. Arimo offers improved 
on-screen readability characteristics and the pan-European WGL character set 
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.

%files -n fonts-ttf-google-croscore-arimo
%{_fontconfig_templatedir}/*-%{fontname}-arimo.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-arimo.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Arimo*.ttf
%{_datadir}/appdata/%{fontname}-arimo.metainfo.xml

%package -n fonts-ttf-google-croscore-cousine
Group: System/Fonts/True type
Summary:       The croscore Cousine family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-google-croscore-cousine
%common_desc
Cousine was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Courier New. Cousine offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.

%files -n fonts-ttf-google-croscore-cousine
%{_fontconfig_templatedir}/*-%{fontname}-cousine.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-cousine.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Cousine*.ttf
%{_datadir}/appdata/%{fontname}-cousine.metainfo.xml

%package -n fonts-ttf-google-croscore-tinos
Group: System/Fonts/True type
Summary:       The croscore Tinos family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n fonts-ttf-google-croscore-tinos
%common_desc
Tinos was designed by Steve Matteson as an innovative, refreshing serif design
that is metrically compatible with Times New Roman. Tinos offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to
address document portability across platforms.

%files -n fonts-ttf-google-croscore-tinos
%{_fontconfig_templatedir}/*-%{fontname}-tinos.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-tinos.conf
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Tinos*.ttf
%{_datadir}/appdata/%{fontname}-tinos.metainfo.xml

%prep
%setup -q -n croscorefonts-%{version}
cp -p %{SOURCE8} .

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-arimo.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-cousine.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-tinos.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-arimo.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-cousine.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-tinos.conf

for fconf in %{fontconf62}-arimo.conf %{fontconf30}-arimo.conf \
             %{fontconf62}-cousine.conf %{fontconf30}-cousine.conf \
             %{fontconf62}-tinos.conf %{fontconf30}-tinos.conf
do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-arimo.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-cousine.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tinos.metainfo.xml
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

%files -n fonts-ttf-google-croscore-common
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.31.0-alt1_2
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_6
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_2
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_1
- applied repocop patches

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.21.0-alt1_4
- update to new release by fcimport

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.21.0-alt1_3
- fc import

