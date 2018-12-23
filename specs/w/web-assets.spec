Group: Development/Other
%filter_from_requires /^.usr.share.fonts$/d
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#disable the httpd stuff while we're waiting on getting the path issues
#cleared up
%global enable_httpd 0

Name:           web-assets
Version:        5
Release:        alt3_6
Summary:        A simple framework for bits pushed to browsers
BuildArch:      noarch

License:        MIT
URL:            https://fedoraproject.org/wiki/User:Patches/PackagingDrafts/Web_Assets

Source1:        LICENSE
Source2:        macros.web-assets
Source3:        web-assets.conf
Source4:        README.devel
Source44: import.info

%description
%{summary}.

%package filesystem
Group: Other
Summary:        The basic directory layout for Web Assets
#there's nothing copyrightable about a few directories and symlinks
License:        ALT-Public-Domain

%description filesystem
%{summary}.

%package -n rpm-macros-%name
Group: Other
Summary:        RPM macros for Web Assets packaging
License:        MIT
Provides: %name-devel = %{?epoch:%epoch:}%{version}-%{release}

%description -n rpm-macros-%name
%{summary}.

%if 0%{?enable_httpd}
%package httpd
Group: Other
Summary:        Web Assets aliases for the Apache HTTP daemon
License:        MIT
Requires:       web-assets-filesystem = %{version}-%{release}
Requires:       apache-base apache2-base apache2-htcacheclean

%description httpd
%{summary}.
%endif

%prep
%setup -c -T
cp %{SOURCE1} LICENSE
cp %{SOURCE4} README.devel

%build
#nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/web-assets
mkdir -p %{buildroot}%{_datadir}/javascript

ln -sf ../javascript %{buildroot}%{_datadir}/web-assets/javascript
ln -sf ../javascript %{buildroot}%{_datadir}/web-assets/js
ln -sf ../fonts %{buildroot}%{_datadir}/web-assets/fonts

install -Dpm0644 %{SOURCE2} %{buildroot}%{_rpmmacrosdir}/web-assets

%if 0%{?enable_httpd}
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d/web-assets.conf

%endif
%files filesystem
%{_datadir}/web-assets
%{_datadir}/javascript

%files -n rpm-macros-%name
%{_rpmmacrosdir}/web-assets
%doc LICENSE README.devel

%if 0%{?enable_httpd}
%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/web-assets.conf
%doc LICENSE
%endif

%changelog
* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 5-alt3_6
- update to new release by fcimport

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 5-alt3_4
- added rpm-macros-web-assets

* Thu Dec 31 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt3_3
- to Sisyphus as BR: for mathjax

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt2_3
- rebuild

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt1_3
- new version

