%define  pkgname graphviz

Name:    ruby-%pkgname
Version: 1.1.0
Release: alt1

Summary: A ruby interface for GraphViz graph visualisation toolkit
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/ioquatix/graphviz

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
%doc README* examples/
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
