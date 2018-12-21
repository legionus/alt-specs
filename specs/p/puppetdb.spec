Name:     puppetdb
Version:  6.0.1
Release:  alt1

Summary:  Centralized Puppet Storage
License:  Apache-2.0
Group:    Other
Url:      https://github.com/puppetlabs/puppetdb

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildArch:      noarch

BuildPreReq: /proc rpm-build-java rpm-build-ruby rpm-build-ubt

Requires: puppet
Requires: postgresql
Requires: clojure
Requires: ruby-msgpack

%def_enable initd

%description
PuppetDB is the fast, scalable, and reliable data warehouse for Puppet. It
caches data generated by Puppet, and gives you advanced features at awesome
speed with a powerful API.

%package terminus
Summary: PuppetDB Ruby plug-in
Group: Development/Ruby

%description terminus
PuppetDB Ruby plug-in

%prep
%setup

%install
install -D %name.jar %buildroot%_javadir/%name/%name.jar
install -D %name.service %buildroot%_unitdir/%name.service

%if_enabled initd
install -D %name.init %buildroot%_initdir/%name
mkdir -p %buildroot%_sysconfdir/tmpfiles.d
cat >%buildroot%_sysconfdir/tmpfiles.d/%name.conf <<EOF
d /var/run/puppetdb 0775 _puppetdb _puppetdb -
EOF
mkdir -p %buildroot%_runtimedir/%name
%endif

mkdir -p %buildroot%_sysconfdir/sysconfig
touch %buildroot%_sysconfdir/sysconfig/%name

install -D default %buildroot%_sysconfdir/default/%name

install -Dm 0755 cli/%name %buildroot%_bindir/%name

install -d -m 0755 %buildroot%_sysconfdir/%name/conf.d
install -d -m 0755 %buildroot%_javadir/%name/cli
install -d -m 0755 %buildroot%_javadir/%name/cli/apps
install -d -m 0755 %buildroot%_logdir/%name
install -d -m 0755 %buildroot%_localstatedir/%name

install request-logging.xml %buildroot%_sysconfdir/%name/request-logging.xml
install jetty.ini %buildroot%_sysconfdir/%name/conf.d/jetty.ini
install config.ini %buildroot%_sysconfdir/%name/conf.d/config.ini
install repl.ini %buildroot%_sysconfdir/%name/conf.d/repl.ini
install database.ini %buildroot%_sysconfdir/%name/conf.d/database.ini
install bootstrap.cfg %buildroot%_sysconfdir/%name/bootstrap.cfg
install logback.xml %buildroot%_sysconfdir/%name/logback.xml

install -m 0755 cli/reload %buildroot%_javadir/%name/cli/apps/reload
install -m 0755 cli/foreground %buildroot%_javadir/%name/cli/apps/foreground
install -m 0755 cli/start %buildroot%_javadir/%name/cli/apps/start
install -m 0755 cli/stop %buildroot%_javadir/%name/cli/apps/stop
install -m 0755 cli/anonymize %buildroot%_javadir/%name/cli/apps/anonymize
install -m 0755 cli/ssl-setup %buildroot%_javadir/%name/cli/apps/ssl-setup
install -m 0755 cli/config-migration %buildroot%_javadir/%name/cli/apps/config-migration
install -m 0755 cli/foreground %buildroot%_javadir/%name/cli/apps/foreground
install -m 0755 cli/upgrade %buildroot%_javadir/%name/cli/apps/upgrade

install -Dm 0644 puppet/reports/puppetdb.rb %buildroot%ruby_sitelibdir/puppet/reports/puppetdb.rb
install -Dm 0644 puppet/indirector/resource/puppetdb.rb %buildroot%ruby_sitelibdir/puppet/indirector/resource/puppetdb.rb
install -Dm 0644 puppet/indirector/node/puppetdb.rb %buildroot%ruby_sitelibdir/puppet/indirector/node/puppetdb.rb
install -Dm 0644 puppet/indirector/catalog/puppetdb.rb %buildroot%ruby_sitelibdir/puppet/indirector/catalog/puppetdb.rb
install -Dm 0644 puppet/indirector/facts/puppetdb_apply.rb %buildroot%ruby_sitelibdir/puppet/indirector/facts/puppetdb_apply.rb
install -Dm 0644 puppet/indirector/facts/puppetdb.rb %buildroot%ruby_sitelibdir/puppet/indirector/facts/puppetdb.rb
install -Dm 0644 puppet/util/puppetdb.rb %buildroot%ruby_sitelibdir/puppet/util/puppetdb.rb
install -Dm 0644 puppet/util/puppetdb/atom.rb %buildroot%ruby_sitelibdir/puppet/util/puppetdb/atom.rb
install -Dm 0644 puppet/util/puppetdb/command_names.rb %buildroot%ruby_sitelibdir/puppet/util/puppetdb/command_names.rb
install -Dm 0644 puppet/util/puppetdb/command.rb %buildroot%ruby_sitelibdir/puppet/util/puppetdb/command.rb
install -Dm 0644 puppet/util/puppetdb/http.rb %buildroot%ruby_sitelibdir/puppet/util/puppetdb/http.rb
install -Dm 0644 puppet/util/puppetdb/char_encoding.rb %buildroot%ruby_sitelibdir/puppet/util/puppetdb/char_encoding.rb
install -Dm 0644 puppet/util/puppetdb/config.rb %buildroot%ruby_sitelibdir/puppet/util/puppetdb/config.rb
install -Dm 0644 puppet/face/node/deactivate.rb %buildroot%ruby_sitelibdir/puppet/face/node/deactivate.rb
install -Dm 0644 puppet/face/node/status.rb %buildroot%ruby_sitelibdir/puppet/face/node/status.rb
install -Dm 0644 puppet/functions/puppetdb_query.rb %buildroot%ruby_sitelibdir/puppet/functions/puppetdb_query.rb

install -m 0755 ezbake-functions.sh %buildroot%_javadir/%name/ezbake-functions.sh
install -m 0644 ezbake.manifest %buildroot%_javadir/%name/ezbake.manifest

%pre
getent group _puppetdb > /dev/null || groupadd -r _puppetdb || :
useradd -r --gid _puppetdb --home %_localstatedir/%name --shell $(which nologin) \
    --comment "puppetdb daemon"  _puppetdb || :

%files
%_javadir/%name/*
%_unitdir/%name.service
%dir %_sysconfdir/%name
%dir %attr(0770,_puppetdb,_puppetdb) %_localstatedir/%name
%if_enabled initd
%_initdir/%name
%_sysconfdir/tmpfiles.d/%name.conf
%_runtimedir/%name
%doc docs/%name/*
%endif
%dir %_javadir/%name
%dir %attr(0770,_puppetdb,_puppetdb) %_logdir/%name
%dir %_sysconfdir/%name/conf.d
%dir %_javadir/%name/cli
%dir %_javadir/%name/cli/apps
%_javadir/%name/cli/apps/*
%_bindir/*

%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/sysconfig/%name
%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/default/%name
%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/%name/request-logging.xml
%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/%name/conf.d/jetty.ini
%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/%name/conf.d/config.ini
%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/%name/conf.d/repl.ini
%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/%name/conf.d/database.ini
%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/%name/bootstrap.cfg
%config(noreplace) %attr(0660,_puppetdb,_puppetdb) %_sysconfdir/%name/logback.xml

%files terminus
%ruby_sitelibdir/*

%changelog
* Fri Nov 09 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.1-alt1
- Update version to 6.0.1

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.4-alt1.S1.1
- Rebuild for new Ruby autorequirements.

* Tue Jul 31 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.2.4-alt1%ubt
- Update version to 5.2.4

* Mon May 28 2018 Maxim Voronov <mvoronov@altlinux.org> 5.2.2-alt2%ubt
- Use ubt macro

* Fri May 18 2018 Maxim Voronov <mvoronov@altlinux.org> 5.2.2-alt1
- Update to 5.2.2

* Wed Dec 27 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.1.3-alt1
- Update to 5.1.3 and fully repack

* Wed Nov 29 2017 Mikhail Gordeev <obirvalger@altlinux.org> 4.4.0-alt2
- Currently does not support start option because of puppetserver needed

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 4.4.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon May 22 2017 Gordeev Mikhail <obirvalger@altlinux.org> 4.4.0-alt1
- Initial build in Sisyphus
