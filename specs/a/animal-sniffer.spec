Name:    animal-sniffer
Version: 1.17
Release: alt1
Summary: The Animal Sniffer Plugin is used to build signatures of APIs and to check your classes against previously generated signatures

Group:   Development/Java
License: MIT
URL:     https://github.com/mojohaus/animal-sniffer
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven-local
BuildRequires:  mojo-parent
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-project
BuildRequires:  maven-toolchain
BuildRequires:  maven-shade-plugin

BuildArch: noarch
Requires: java >= 1.6.0

%description
The Animal Sniffer Plugin is used to build signatures of APIs and to
check your classes against previously generated signatures. This plugin
is called animal sniffer because the principal signatures that are used
are those of the Java Runtime, and since Sun traditionally names the
different versions of its Java Runtimes after different animals, the
plugin that detects what Java Runtime your code requires was called
"Animal Sniffer".

%package javadoc
Summary:  Javadoc for %name
Group:    Documentation
Requires: jpackage-utils

Requires: jpackage-utils
Requires: %name = %version-%release

%description javadoc
Javadoc for %name.

%prep
%setup

%build
%mvn_build

%install
%mvn_install
install -Dpm 644 pom.xml %buildroot%_mavenpomdir/JPP-%name.pom

%files -f .mfiles
%doc README.md
%_mavenpomdir/*

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.17-alt1
- Initial build for Sisyphus
