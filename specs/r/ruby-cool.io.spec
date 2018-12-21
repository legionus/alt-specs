%define  pkgname cool.io

Name:    ruby-%pkgname
Version: 1.5.3
Release: alt1

Summary: Simple evented I/O for Ruby (but please check out Celluloid::IO instead)
License: MIT
Group:   Development/Ruby
Url:     https://github.com/tarcieri/cool.io/

Packager:  Mikhail Gordeev <obirvalger@altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Sep 29 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.3-alt1
- Initial build for Sisyphus
