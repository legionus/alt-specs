Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          glassfish-fastinfoset
Version:       1.2.13
Release:       alt1_9jpp8
Summary:       Fast Infoset
License:       ASL 2.0
URL:           https://fi.java.net
# svn export https://svn.java.net/svn/fi~svn/tags/fastinfoset-project-1.2.13/ glassfish-fastinfoset-1.2.13
# find glassfish-fastinfoset-1.2.13/ -name '*.class' -delete
# find glassfish-fastinfoset-1.2.13/ -name '*.jar' -delete
# rm -rf glassfish-fastinfoset-1.2.13/roundtrip-tests
# tar czf glassfish-fastinfoset-1.2.13-src-svn.tar.gz glassfish-fastinfoset-1.2.13
Source0:       %{name}-%{version}-src-svn.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
# add xmlstreambuffer 1.5.x support
Patch0:        %{name}-1.2.12-utilities-FastInfosetWriterSAXBufferProcessor.patch

BuildRequires: maven-local
BuildRequires: mvn(com.sun.xml.stream.buffer:streambuffer)
BuildRequires: mvn(com.sun.xsom:xsom)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:     noarch
Source44: import.info

%description
Fast Infoset specifies a standardized binary encoding for the XML Information
Set. An XML infoset (such as a DOM tree, StAX events or SAX events in
programmatic representations) may be serialized to an XML 1.x document or, as
specified by the Fast Infoset standard, may be serialized to a fast infoset
document.  Fast infoset documents are generally smaller in size and faster to
parse and serialize than equivalent XML documents.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0

cp %{SOURCE1} .

# Remove wagon-webdav
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-antrun-extended-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin

%pom_disable_module roundtrip-tests
%pom_disable_module samples

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
 <execution>
  <id>default-jar</id>
  <phase>skip</phase>
 </execution>" fastinfoset

%mvn_file :FastInfoset %{name}
%mvn_file :FastInfosetUtilities %{name}-utilities

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference copyright.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference copyright.txt LICENSE-2.0.txt

%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.13-alt1_9jpp8
- java fc28+ update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.13-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.13-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.13-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.13-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.13-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.13-alt1_3jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt5_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt5_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt4_4jpp7
- bugfix in alternative

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt3_4jpp7
- rised priority of alternative

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt2_4jpp7
- shared FastInfoset.jar symlink as alternative

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt1_4jpp7
- new version

