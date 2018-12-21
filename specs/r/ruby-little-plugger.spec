%define  pkgname little-plugger

Name:    ruby-%pkgname
Version: 1.1.4
Release: alt1.1

Summary: A gems based plugin framework for Ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://github.com/TwP/little-plugger

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Source1: %pkgname.gemspec

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
LittlePlugger is a module that provides Gem based plugin management. By
extending your own class or module with LittlePlugger you can easily
manage the loading and initializing of plugins provided by other gems.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
cp %SOURCE1 %pkgname.gemspec
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
* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1.1
- Rebuild for new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- New version.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
