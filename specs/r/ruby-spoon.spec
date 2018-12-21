%define  pkgname spoon

Name: 	 ruby-%pkgname
Version: 0.0.6 
Release: alt1.1

Summary: A fork/exec replacement for FFI-capable implementations
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/headius/spoon

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
A fork/exec replacement for FFI-capable implementations.

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
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.0.6-alt1
- Initial build in Sisyphus
