%define oldname taipeifonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name taipeifonts
%define fontname taipeifonts
%define common_desc Traditional Chinese Bitmap fonts

%define bmpfontdir    %{_datadir}/fonts/bitmap/%{oldname}
%define catalogue     /etc/X11/fontpath.d

Name:       fonts-bitmap-taipei
Version:    1.2
Release:    alt1_22
Summary:    %common_desc

Group:      Graphical desktop/Other
License:    ALT-Public-Domain
URL:        http://cle.linux.org.tw/

BuildArch:        noarch
BuildRequires:    bdftopcf fonttosfnt mkfontdir mkfontscale xorg-font-utils

Source0:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{oldname}-%{version}/%{oldname}-%{version}.tar.gz
Source1:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{oldname}-%{version}/%{oldname}.alias
Source2:    ftp://cle.linux.org.tw/pub/CLE/devel/wjwu/slackware/slackware-10.0/source/%{oldname}-%{version}/re-build.readme
Source44: import.info

%description
%common_desc

%prep
%setup -n %{oldname}-%{version} -q
cp -p %SOURCE2 README

%build
bdftopcf taipei24.bdf | gzip -c > taipei24.pcf.gz
bdftopcf taipei20.bdf | gzip -c > taipei20.pcf.gz
bdftopcf taipei16.bdf | gzip -c > taipei16.pcf.gz

%install

install -d $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei24.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei20.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 taipei16.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 vga12x24.pcf.gz $RPM_BUILD_ROOT%{bmpfontdir}
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{bmpfontdir}/fonts.alias

mkfontdir $RPM_BUILD_ROOT%{bmpfontdir}

# catalogue
install -d $RPM_BUILD_ROOT%{catalogue}
ln -s %{bmpfontdir} $RPM_BUILD_ROOT%{catalogue}/%{oldname}

%files
%doc README
%dir %{bmpfontdir}
%{bmpfontdir}/*.gz
%{bmpfontdir}/fonts.alias
%verify(not md5 size mtime) %{bmpfontdir}/fonts.dir
%{catalogue}/%{oldname}

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_22
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_18
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_16
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_15
- update to new release by fcimport

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_14
- fc import

