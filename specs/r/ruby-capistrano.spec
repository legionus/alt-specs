Name: ruby-capistrano
Version: 2.5.10
Release: alt1.3

Summary: Capistrano -- Welcome to easy deployment with Ruby over SSH
Group: Development/Ruby
License: MIT
Url: http://github.com/capistrano/capistrano
Source0: capistrano.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 12 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Capistrano is a utility and framework for executing commands in parallel on
multiple remote machines, via SSH.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name.

%prep
%setup -q -n capistrano
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

rm -f %buildroot%ruby_sitelibdir/capistrano/recipes/compat.rb

%files
%doc CHANGELOG.rdoc README.rdoc
%_bindir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Capistrano

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.10-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.10-alt1.2
- Rebuild with Ruby 2.4.1

* Fri Dec 07 2012 Led <led@altlinux.ru> 2.5.10-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 2.5.10-alt1
- build for Sisyphus

