%define  pkgname google-api-ruby-client

Name:    ruby-google-api
Version: 0.25.0
Release: alt1

Summary: Google API Client for Ruby
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/google/google-api-ruby-client

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(java\|rails/d

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
cp -a generated/* %buildroot%ruby_sitelibdir/
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc *.md
%_bindir/generate-api
%ruby_sitelibdir/*
%rubygem_specdir/*.gemspec

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 0.25.0-alt1
- New version.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.24.2-alt1
- New version.

* Mon Sep 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.24.1-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.24.0-alt1
- New version.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.23.0-alt1
- New version.
- Package as gem.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.22.0-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.21.2-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt1
- Initial build for Sisyphus
