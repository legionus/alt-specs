%define  pkgname azure

Name: 	 ruby-%pkgname
Version: 0.7.10
Release: alt2.1

Summary: Microsoft Azure Client Library for Ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/azure/azure-sdk-for-ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Official Ruby client library to consume Microsoft Azure services.

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
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.10-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.10-alt2
- Disable tests.

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.10-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.9-alt1
- Initial build for ALT Linux
