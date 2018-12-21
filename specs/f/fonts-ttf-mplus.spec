%define oldname mplus-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
###############################################################################
# Definitions
###############################################################################
%global fixed_desc() \
The combination of fixed-fullwidth M+ %2 for Japanese and fixed-halfwidth \
%1 %2 %3 for alphabets. They are 5 weights from Thin to Bold.   

%global proportional_desc() \
The combination of fixed-fullwidth M+ %2 for Japanese and proportional  \
%1 %2 %3 for alphabets. They are 7 weights from Thin to Black.         

%global common_desc() \
The Mplus fonts are 7 families of fonts, of which 4 are combinations \
of proportional font families,variations of fixed-fullwidth fonts, \
variations of fixed-halfwidth fonts and each have between 5 - 7 \
different weights.

%global summary_p M+ P is aimed as sophisticated and relaxed design

%global summary_c M+ C is optimized to be proportioned and has two variations

%global summary_m M+ M emphasize the balance of natural letterform and high legibility


%global fontname mplus

###############################################################################
# Header
###############################################################################

Name:       fonts-ttf-mplus
Version:    056
Release:    alt1_7
Summary:    The Mplus fonts is a superfamily of fonts designed by Coji Morishita

Group:      System/Fonts/True type
License:    mplus
URL:        http://%{fontname}-fonts.sourceforge.jp/%{fontname}-outline-fonts/index-en.html
Source0:    http://dl.sourceforge.jp/%{fontname}-fonts/6650/%{fontname}-TESTFLIGHT-%{version}.tar.xz

BuildArch: noarch  
BuildRequires:   fontpackages-devel  
Source44: import.info

%description
%common_desc

###############################################################################
# Package section
###############################################################################

%package -n fonts-ttf-mplus-common
Group: System/Fonts/True type
Summary:  Mplus, common files (documentationa..)

%description -n fonts-ttf-mplus-common
%common_desc

This package consists of files used by other %{oldname} packages.


# 1p
%package -n fonts-ttf-mplus-1p
Group: System/Fonts/True type
Summary: %summary_p
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-1p
%proportional_desc M+ 1P Type-1

%files -n fonts-ttf-mplus-1p
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-1p-*.ttf
%{_datadir}/appdata/mplus-1p.metainfo.xml

# 2p
%package -n fonts-ttf-mplus-2p
Group: System/Fonts/True type
Summary: %summary_p
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-2p
%proportional_desc M+ 2P Type-2

%files -n fonts-ttf-mplus-2p
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-2p-*.ttf
%{_datadir}/appdata/%{fontname}-2p.metainfo.xml

# 1c
%package -n fonts-ttf-mplus-1c
Group: System/Fonts/True type
Summary: %summary_c
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-1c
%proportional_desc M+ 1C Type-1

%files -n fonts-ttf-mplus-1c
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-1c-*.ttf
%{_datadir}/appdata/%{fontname}-1c.metainfo.xml

# 2c
%package -n fonts-ttf-mplus-2c
Group: System/Fonts/True type
Summary: %summary_c
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-2c
%proportional_desc M+ 2C Type-2

%files -n fonts-ttf-mplus-2c
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-2c-*.ttf
%{_datadir}/appdata/%{fontname}-2c.metainfo.xml

# 1m
%package -n fonts-ttf-mplus-1m
Group: System/Fonts/True type
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-1m
%fixed_desc M+ 1M Type-1

%files -n fonts-ttf-mplus-1m
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-1m-*.ttf
%{_datadir}/appdata/%{fontname}-1m.metainfo.xml

# 2m
%package -n fonts-ttf-mplus-2m
Group: System/Fonts/True type
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-2m
%fixed_desc M+ 2M Type-2

%files -n fonts-ttf-mplus-2m
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-2m-*.ttf
%{_datadir}/appdata/%{fontname}-2m.metainfo.xml

# 1mn
%package -n fonts-ttf-mplus-1mn
Group: System/Fonts/True type
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n fonts-ttf-mplus-1mn
%fixed_desc M+ 1MN Type-1

%files -n fonts-ttf-mplus-1mn
%{_fontbasedir}/*/%{_fontstem}/%{fontname}-1mn-*.ttf
%{_datadir}/appdata/%{fontname}-1mn.metainfo.xml

###############################################################################
# Files
###############################################################################
%prep
%setup -q -n %{fontname}-TESTFLIGHT-%{version}

%build

%install

# Add AppStream metadata
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-1c.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1c</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1C</name>
  <summary>A font which is optimized to be proportioned</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-2c.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-2c</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1C</name>
  <summary>A font which is optimized to be proportioned</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-1m.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1m</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1M</name>
  <summary>A font which emphasizes the balance of natural letterform with high legibility</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-1mn.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1mn</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1MN</name>
  <summary>A font which emphasizes the balance of natural letterform with high legibility</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-1p.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1p</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1P</name>
  <summary>A font which is aimed as sophisticated and relaxed design</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-2p.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1p</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 2P</name>
  <summary>A font which is aimed as sophisticated and relaxed design</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-2m.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-2m</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 2M</name>
  <summary>A font which emphasizes the balance of natural letterform with high legibility</summary>
</component>
EOF

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
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

%files -n fonts-ttf-mplus-common
%doc LICENSE_E README_{E,J}
%doc LICENSE_J README_{E,J}

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 056-alt1_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 028-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 028-alt3_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 028-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 028-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 028-alt2_2
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 028-alt1_2
- initial release by fcimport

