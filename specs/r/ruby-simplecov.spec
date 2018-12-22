%define  pkgname simplecov
 
Name: 	 ruby-%pkgname
Version: 0.16.1
Release: alt1.1
 
Summary: Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites
License: MIT or Ruby
Group:   Development/Ruby
Url:     https://github.com/colszowka/simplecov
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires \,^ruby(\(jruby\|simplecov/railties/tasks.rake\),d

%description
SimpleCov is a code coverage analysis tool for Ruby. It uses Ruby's
built-in Coverage library to gather code coverage data, but makes
processing its results much easier by providing a clean API to filter,
group, merge, format, and display those results, giving you a complete
code coverage suite that can be set up with just a couple lines of code.

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
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version.

* Thu Feb 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt0.M70C.1
- Rebuild with Ruby 2.4.3

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt1
- New version

* Tue Aug 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.1-alt1
- New version

* Fri Mar 17 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt2
- Rebuild with missing requirements

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- Initial build in Sisyphus
