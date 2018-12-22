Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          boilerpipe
Version:       1.2.0
Release:       alt1_11jpp8
Summary:       Boilerplate Removal and Fulltext Extraction from HTML pages
License:       Apache-2.0
Url:           https://github.com/kohlschutter/boilerpipe
Source0:       http://boilerpipe.googlecode.com/files/%{name}-%{version}-src.tar.gz
Source1:       http://boilerpipe.googlecode.com/svn/repo/de/l3s/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# use system libraries
Patch0:        %{name}-1.2.0-libdir-patch
# remove embedded nekohtml
Patch1:        %{name}-1.2.0-nekohtml-patch

BuildRequires: ant
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: nekohtml
BuildRequires: xerces-j2

BuildArch:     noarch
Source44: import.info

%description
The boilerpipe library provides algorithms to detect and
remove the surplus "clutter" (boilerplate, templates)
around the main textual content of a web page.

The library already provides specific strategies 
for common tasks (for example: news article extraction) and
may also be easily extended for individual problem settings.

Extracting content is very fast (milliseconds), just needs the
input document (no global or site-level information required) and
is usually quite accurate. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -iname '*.jar' -delete
find . -iname '*.class' -delete

%patch0 -p0
cp %{SOURCE1} pom.xml
%patch1 -p1

# fix non ASCII chars
for s in src/main/de/l3s/boilerpipe/BoilerpipeInput.java \
 src/main/de/l3s/boilerpipe/BoilerpipeInput.java \
 src/main/de/l3s/boilerpipe/BoilerpipeFilter.java \
 src/main/de/l3s/boilerpipe/BoilerpipeExtractor.java \
 src/main/de/l3s/boilerpipe/BoilerpipeProcessingException.java \
 src/main/de/l3s/boilerpipe/conditions/TextBlockCondition.java \
 src/main/de/l3s/boilerpipe/document/TextBlock.java \
 src/main/de/l3s/boilerpipe/document/TextDocumentStatistics.java \
 src/main/de/l3s/boilerpipe/document/TextDocument.java \
 src/main/de/l3s/boilerpipe/estimators/SimpleEstimator.java \
 src/main/de/l3s/boilerpipe/extractors/LargestContentExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/DefaultExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/NumWordsRulesExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/KeepEverythingWithMinKWordsExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/ExtractorBase.java \
 src/main/de/l3s/boilerpipe/extractors/ArticleSentencesExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/CommonExtractors.java \
 src/main/de/l3s/boilerpipe/extractors/CanolaExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/ArticleExtractor.java \
 src/main/de/l3s/boilerpipe/extractors/KeepEverythingExtractor.java \
 src/main/de/l3s/boilerpipe/filters/english/HeuristicFilterBase.java \
 src/main/de/l3s/boilerpipe/filters/english/KeepLargestFulltextBlockFilter.java \
 src/main/de/l3s/boilerpipe/filters/english/TerminatingBlocksFinder.java \
 src/main/de/l3s/boilerpipe/filters/english/IgnoreBlocksAfterContentFilter.java \
 src/main/de/l3s/boilerpipe/filters/english/IgnoreBlocksAfterContentFromEndFilter.java \
 src/main/de/l3s/boilerpipe/filters/english/DensityRulesClassifier.java \
 src/main/de/l3s/boilerpipe/filters/english/MinFulltextWordsFilter.java \
 src/main/de/l3s/boilerpipe/filters/english/NumWordsRulesClassifier.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/SimpleBlockFusionProcessor.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/BlockProximityFusion.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/KeepLargestBlockFilter.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/DocumentTitleMatchClassifier.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/LabelFusion.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/AddPrecedingLabelsFilter.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/ExpandTitleToContentFilter.java \
 src/main/de/l3s/boilerpipe/filters/heuristics/ContentFusion.java \
 src/main/de/l3s/boilerpipe/filters/simple/MinWordsFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/LabelToBoilerplateFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/LabelToContentFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/InvertedFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/InvertedFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/MinClauseWordsFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/BoilerplateBlockFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/SplitParagraphBlocksFilter.java \
 src/main/de/l3s/boilerpipe/filters/simple/MarkEverythingContentFilter.java \
 src/main/de/l3s/boilerpipe/labels/DefaultLabels.java \
 src/main/de/l3s/boilerpipe/labels/ConditionalLabelAction.java \
 src/main/de/l3s/boilerpipe/labels/LabelAction.java \
 src/main/de/l3s/boilerpipe/sax/BoilerpipeSAXInput.java \
 src/main/de/l3s/boilerpipe/sax/HTMLHighlighter.java \
 src/main/de/l3s/boilerpipe/sax/BoilerpipeHTMLContentHandler.java \
 src/main/de/l3s/boilerpipe/sax/BoilerpipeHTMLParser.java \
 src/main/de/l3s/boilerpipe/sax/TagActionMap.java \
 src/main/de/l3s/boilerpipe/sax/InputSourceable.java \
 src/main/de/l3s/boilerpipe/sax/HTMLDocument.java \
 src/main/de/l3s/boilerpipe/sax/CommonTagActions.java \
 src/main/de/l3s/boilerpipe/sax/DefaultTagActionMap.java \
 src/main/de/l3s/boilerpipe/sax/HTMLFetcher.java \
 src/main/de/l3s/boilerpipe/sax/TagAction.java \
 src/main/de/l3s/boilerpipe/sax/MarkupTagAction.java \
 src/main/de/l3s/boilerpipe/util/UnicodeTokenizer.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%build

ant -Dapp.javaversion=1.6

%install
%mvn_artifact pom.xml dist/%{name}-%{version}.jar
%mvn_file de.l3s.%{name}:%{name} %{name}
%mvn_install -J javadoc/1.2

install -pm 644 dist/%{name}-demo-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-demo.jar

%files -f .mfiles
%{_javadir}/%{name}-demo.jar
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_11jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_10jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_7jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_6jpp8
- new version

