%define  pkgname uglifier

Name:    ruby-%pkgname
Version: 4.1.19
Release: alt1

Summary: Ruby wrapper for UglifyJS JavaScript compressor.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/lautis/uglifier

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
%rubygem_specdir/*.gemspec

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.19-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.14-alt2
- Rebuild ro correct gemspec name.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.14-alt1
- New version.
- Package as gem.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.12-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.11-alt1
- Initial build for Sisyphus
