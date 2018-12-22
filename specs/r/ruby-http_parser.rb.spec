%define  pkgname http_parser.rb
 
Name: 	 ruby-%pkgname
Version: 0.6.0 
Release: alt3.5
 
Summary: A simple callback-based HTTP request/response parser for writing http servers, clients and proxies
License: MIT or Ruby
Group:   Development/Ruby
Url:     https://github.com/tmm1/http_parser.rb
 
Packager: Andrey Cherepanov <cas@altlinux.org>
 
Source:  %pkgname-%version.tar
Source1: http-parser-2.3.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup
BuildRequires: ruby-benchmark_suite
BuildRequires: ruby-ffi
BuildRequires: libruby-devel

%description
A simple callback-based HTTP request/response parser for writing http
servers, clients and proxies.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
tar xf %SOURCE1

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
%ruby_sitearchdir/*
%ruby_sitelibdir/*
%rubygem_specdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Sun Aug 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.5
- Rebuild for new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt2
- Rebuild with Ruby 2.3.1

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for ALT Linux
