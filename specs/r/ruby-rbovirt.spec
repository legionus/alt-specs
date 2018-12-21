%define  pkgname rbovirt

Name:    ruby-%pkgname
Version: 0.1.7
Release: alt1

Summary: a ruby client for ovirt
License: MIT
Group:   Development/Ruby
Url:     https://github.com/abenari/rbovirt

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
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.7-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
