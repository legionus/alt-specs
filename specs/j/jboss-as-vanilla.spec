Name: jboss-as-vanilla
Version: 7.1.1
Release: alt14

Summary: jboss-as-vanilla - Vanilla Edition Of JBoss Application Server

License: LGPLv2 and Apache-2.0
Group: System/Servers
Url: http://www.jboss.org/jbossas

#how create git repo from zip
#wget http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-as-7.1.1.Final.zip
#unzip jboss-as-7.1.1.Final.zip
Source: %name-%version.tar
Source1: jboss-as-cp
Source2: jboss-as-vanilla.service

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: java >= 1.7
AutoReq: yes, nomingw, nomingw32
#Provides:
#Conflicts:

#BuildPreReq:
BuildArch: noarch

%define jbossuser jboss-as
#jboss-as:x:185:185:JBoss AS:%_datadir/jboss-as:/bin/nologin
%define jbossdir %_datadir/jboss-as

%description
JBoss Application Server 7 is the latest release in a series of JBoss
Application Server offerings. JBoss Application Server 7, is a fast,
powerful, implementation of the Java Enterprise Edition 6 specification.
The state-of-the-art architecture built on the Modular Service Container
enables services on-demand when your application requires them.

%prep
%setup

%build
#nothing to do

%install
#in jboss-as
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/%jbossdir/
mkdir -p %buildroot/%_initdir/
mkdir -p %buildroot/etc/jboss-as/
mkdir -p %buildroot/lib/systemd/system/

cp %SOURCE1 %buildroot/%_bindir/
cp %SOURCE2 %buildroot/lib/systemd/system/

cp ./bin/init.d/jboss-as-standalone %buildroot/%_initdir/
cp ./bin/init.d/jboss-as.conf %buildroot/etc/jboss-as/jboss-as.conf

cp -a ./* %buildroot/%jbossdir/
rm -f %buildroot/%jbossdir/bin/*\.bat
mkdir -p %buildroot/%jbossdir/docs/examples/properties/
mkdir -p %buildroot/%jbossdir/standalone/data/
mkdir -p %buildroot/%jbossdir/standalone/log/

cp %buildroot/%jbossdir/standalone/configuration/logging.properties %buildroot/%jbossdir/docs/examples/properties/
cp %buildroot/%jbossdir/standalone/configuration/mgmt-users.properties %buildroot/%jbossdir/docs/examples/properties/
cp %SOURCE1 %buildroot/%jbossdir/docs/examples/properties/standalone-web.xml
#TODO FIX remove cp and add ln -s
cp %buildroot/%jbossdir/bin/jboss-cli.sh %buildroot/%_bindir/jboss-cli


#remove library
rm -rf %buildroot/%jbossdir/modules/org/jboss/as/web/main/lib/*
rm -rf %buildroot/%jbossdir/modules/org/hornetq/main/lib/*
chmod 755 %buildroot/%jbossdir/bin/*\.sh

#alt10 fixup
touch %buildroot/%jbossdir/standalone/log/boot.log
#chmod 755 %buildroot/%jbossdir/standalone/log/boot.log
#chown jboss-as %buildroot/%jbossdir/standalone/log/boot.log

#TODO remove it #why jboss need this dir?
#mkdir /usr/src/GNUstep

#TODO rewrite with user cpecified dir or add all users in jboss-as group and chmod 775
#chmod 777 %buildroot/%jbossdir/standalone/data/content
#chown jboss-as %buildroot/%jbossdir/standalone/data/content


%check

%pre
useradd -d %jbossdir -r -s /bin/nologin %jbossuser >/dev/null 2>&1 || :
#chown -R %jbossuser %jbossdir

%files
%attr(755,%jbossuser,root) %jbossdir/
%attr(755,root,root) %_bindir/jboss-cli
%attr(755,root,root) %_bindir/jboss-as-cp
%attr(755,root,root) /etc/jboss-as/jboss-as.conf
%attr(755,root,root) %_initdir/*
%attr(644,root,root) /lib/systemd/system/jboss-as-vanilla.service

%changelog
* Thu Mar 26 2015 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt14
- Fix JBOSS_BASE_DIR in jboss-as-cp

* Thu Feb 26 2015 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt13
- alt13 fix chown

* Tue Feb 24 2015 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt12
- alt12 fix chown %jbossuser

* Thu Feb 19 2015 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt11
- alt11 small fix standalone running permissions

* Mon Oct 06 2014 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt10
- added set owner to jboss dir
- remove req mingw32

* Mon Sep 29 2014 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt9
- remove chown

* Mon Sep 29 2014 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt8
- added deroctory and fix init script

* Fri Sep 26 2014 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt7
- remove mingw req

* Tue Sep 23 2014 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt6
- fix start by init.d

* Mon Mar 31 2014 Danil Mikhailov <danil@altlinux.org> 7.1.1-alt1
- jboss-as binary from jboss.org without build
