Group: Development/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global revision 1688630
%global date     20150701

Name:           amqp
Version:        1.0
Release:        alt1_9.%{date}svn%{revision}
# increase Epoch to 1 cause of modified Release logic
Epoch:          1
Summary:        The AMQP specification

# Fedora treats these files as content, not code.
# The AMQP license does not give the right to modify.
License:        ASL 2.0

URL:            http://www.amqp.org
Source0:        %{name}-%{version}-%{revision}.tar.gz
# svn export -r %{revision} http://svn.apache.org/repos/asf/qpid/trunk/qpid/specs /tmp/%{name}-%{version}
# cd /tmp ; tar czf %{name}-%{version}-%{revision}.tar.gz /tmp/%{name}-%{version}

BuildArch:      noarch
BuildRequires:  libxslt xsltproc
Source44: import.info

%description
The AMQP (advanced message queuing protocol) specification in XML format.

%package devel
Group: Development/Other
Summary: Development files for %{name}
# be careful with epoch!
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
%{summary}.


%prep
%setup -q

%build
find . -name \*.xml -exec xsltproc -o '{}.html' %{name}.xsl '{}' \;
rename -v '.xml' '' *.html

%install
install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -p -m0644 *.xml *.dtd %{buildroot}%{_datadir}/%{name}

%files
%doc --no-dereference LICENSE
%doc NOTICE MOVED_FILE
%doc *.html

%files devel
%doc --no-dereference LICENSE
%{_datadir}/%{name}/


%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_9.20150701svn1688630
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_8.20150701svn1688630
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_7.20150701svn1688630
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_6.20150701svn1688630
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_5.20150701svn1688630
- update to new release by fcimport

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_4.20150701svn1688630
- to Sisyphus

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.819819-alt2_7
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.819819-alt2_6
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.819819-alt2_5
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.819819-alt2_4
- update to new release by fcimport

* Tue May 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.819819-alt2_3
- regenerated with 0.46 R::S::C

* Fri May 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.819819-alt1_3
- converted for Sisyphus

