%define  pkgname fog-dnsimple

Name:    ruby-%pkgname
Version: 1.0.0
Release: alt1
Epoch:   1

Summary: Module for the 'fog' gem to support DNSimple.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/fog/fog-dnsimple

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

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
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.0.0-alt1
- Reset to old version for fog.

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
