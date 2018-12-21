%define  pkgname net-http-pipeline

Name:    ruby-%pkgname
Version: 1.0.1
Release: alt1.1

Summary: An HTTP/1.1 pipelining implementation atop Net::HTTP
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/drbrain/net-http-pipeline

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-hoe

%description
An HTTP/1.1 pipelining implementation atop Net::HTTP.  A pipelined connection
sends multiple requests to the HTTP server without waiting for the responses.
The server will respond in-order.

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
rake debug_gem > %pkgname.gemspec

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
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
