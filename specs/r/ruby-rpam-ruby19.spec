%define  pkgname rpam-ruby19

Name: 	 ruby-%pkgname
Version: 1.2.2 
Release: alt1.gitbc66d5e.7

Summary: PAM auth for Ruby - 1.9 compat version
License: GPLv2
Group:   Development/Ruby
Url:     https://github.com/canweriotnow/rpam-ruby19

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel
BuildRequires: ruby-tool-setup
BuildRequires: libpam0-devel

%description
This extension provides PAM (Pluggable Authentication Modules) integration. The
library provides a stable API for applications to defer to for authentication
tasks.

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
%doc README* examples
%ruby_sitelibdir/rpam.rb
%ruby_sitearchdir/*
%rubygem_specdir/*.gemspec

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.7
- Fix package as gem.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.6
- Rebuild for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.5
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.4
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.3
- Rebuild for really put gemspec to correct place with Ruby 2.4.2

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e.1
- Rebuild with Ruby 2.4.1

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1.gitbc66d5e
- Initial build in Sisyphus
