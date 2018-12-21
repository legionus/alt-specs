# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname daemons

Name: ruby-%pkgname
Version: 1.2.6
Release: alt1

Summary: A toolkit to create and control daemons in different ways
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/daemons/

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Daemons provides an easy way to wrap existing ruby scripts (for
example a self-written server) to be run as a daemon and to be
controlled by simple start/stop/restart commands.

You can also call blocks as daemons and control them from the
parent or just daemonize the current process.

Besides this basic functionality, daemons offers many advanced
features like exception backtracing and logging (in case your
ruby script crashes) and monitoring and automatic restarting of
your processes if they crash.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%doc examples
%ruby_ri_sitedir/Daemon*

%changelog
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.2
- Rebuild for new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.1.0-alt1
- [1.1.0]

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.10-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 1.0.10-alt1
- Built for Sisyphus

