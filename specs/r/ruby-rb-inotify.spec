%define  pkgname rb-inotify

Name: 	 ruby-%pkgname
Version: 0.9.10
Release: alt2.1

Summary: A thorough inotify wrapper for Ruby using FFI.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/guard/rb-inotify/

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
* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.10-alt2.1
- Rebuild for new Ruby autorequirements.

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.9.10-alt2
- Rebuild as ruby gem for openqa

* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.10-alt1
- Initial build for Sisyphus
