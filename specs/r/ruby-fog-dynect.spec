%define  pkgname fog-dynect

Name:    ruby-%pkgname
Version: 0.0.3
Release: alt1
Epoch:   1

Summary: Module for the 'fog' gem to support Dyn Managed DNS http://dyn.com/
License: MIT
Group:   Development/Ruby
Url:     https://github.com/fog/fog-dynect

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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.0.3-alt1
- Reset to old version for fog.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.2
- Rebuild for new Ruby autorequirements.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
