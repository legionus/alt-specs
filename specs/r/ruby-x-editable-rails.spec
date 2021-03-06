%define  pkgname x-editable-rails

Name:    ruby-%pkgname
Version: 1.5.5.1
Release: alt2.1

Summary: Edit fields easily with X-Editable helper
License: MIT
Group:   Development/Ruby
Url:     https://github.com/werein/x-editable-rails

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
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt2
- Disable tests.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt1
- New version.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5-alt1
- Initial build for Sisyphus
