## GitHub crawler

Simple crawler to get all GitHub repos of a given set of 
organizations that declare 'Java' as their programming language.
You can add more organizations to org_list.txt.

The script will ask you for your GitHub credentials because there is only a small number of API queries that you can make without being authenticated. The script doesn't store your credentials anywhere.

Below is the list of repos it finds for the current org_list:


Reading orgs from /Users/schaef/git/PASCALI/github_crawl/org_list.txt
  total repos for google: 30
truth: https://github.com/google/truth.git	 has travis:True
googletv-android-samples: https://github.com/google/googletv-android-samples.git	 has travis:False
dagger: https://github.com/google/dagger.git	 has travis:True
  total repos for twitter: 30
elephant-bird: https://github.com/twitter/elephant-bird.git	 has travis:True
joauth: https://github.com/twitter/joauth.git	 has travis:True
  total repos for square: 30
fundraiser: https://github.com/square/fundraiser.git	 has travis:False
retrofit: https://github.com/square/retrofit.git	 has travis:True
pad: https://github.com/square/pad.git	 has travis:False
  total repos for netflix: 30
astyanax: https://github.com/Netflix/astyanax.git	 has travis:False
curator: https://github.com/Netflix/curator.git	 has travis:False
Priam: https://github.com/Netflix/Priam.git	 has travis:False
CassJMeter: https://github.com/Netflix/CassJMeter.git	 has travis:False
servo: https://github.com/Netflix/servo.git	 has travis:True
exhibitor: https://github.com/Netflix/exhibitor.git	 has travis:False
gradle-template: https://github.com/Netflix/gradle-template.git	 has travis:False
archaius: https://github.com/Netflix/archaius.git	 has travis:False
SimianArmy: https://github.com/Netflix/SimianArmy.git	 has travis:True
governator: https://github.com/Netflix/governator.git	 has travis:False
netflix-commons: https://github.com/Netflix/netflix-commons.git	 has travis:False
eureka: https://github.com/Netflix/eureka.git	 has travis:False
frigga: https://github.com/Netflix/frigga.git	 has travis:False
blitz4j: https://github.com/Netflix/blitz4j.git	 has travis:False
Hystrix: https://github.com/Netflix/Hystrix.git	 has travis:True
Turbine: https://github.com/Netflix/Turbine.git	 has travis:True
ribbon: https://github.com/Netflix/ribbon.git	 has travis:False
denominator: https://github.com/Netflix/denominator.git	 has travis:True
karyon: https://github.com/Netflix/karyon.git	 has travis:True
EVCache: https://github.com/Netflix/EVCache.git	 has travis:False
recipes-rss: https://github.com/Netflix/recipes-rss.git	 has travis:False
netflix-graph: https://github.com/Netflix/netflix-graph.git	 has travis:False
zuul: https://github.com/Netflix/zuul.git	 has travis:True
suro: https://github.com/Netflix/suro.git	 has travis:False
  total repos for dropbox: 30
dropbox-sdk-java: https://github.com/dropbox/dropbox-sdk-java.git	 has travis:False
pem-converter-maven-plugin: https://github.com/dropbox/pem-converter-maven-plugin.git	 has travis:False
ClickTheBox-android: https://github.com/dropbox/ClickTheBox-android.git	 has travis:False
  total repos for box: 30
box-android-apptoapp-sdk: https://github.com/box/box-android-apptoapp-sdk.git	 has travis:False
metrics: https://github.com/box/metrics.git	 has travis:False
opentsdb: https://github.com/box/opentsdb.git	 has travis:True
tsquery: https://github.com/box/tsquery.git	 has travis:True
asynchbase: https://github.com/box/asynchbase.git	 has travis:False
curator: https://github.com/box/curator.git	 has travis:False
  total repos for facebook: 30
facebook-android-sdk: https://github.com/facebook/facebook-android-sdk.git	 has travis:True
swift: https://github.com/facebook/swift.git	 has travis:False
nifty: https://github.com/facebook/nifty.git	 has travis:False
jcommon: https://github.com/facebook/jcommon.git	 has travis:False
presto: https://github.com/facebook/presto.git	 has travis:True
giraph: https://github.com/facebook/giraph.git	 has travis:False
buck: https://github.com/facebook/buck.git	 has travis:True
  total repos for commoncrawl: 20
commoncrawl-crawler: https://github.com/commoncrawl/commoncrawl-crawler.git	 has travis:False
commoncrawl-examples: https://github.com/commoncrawl/commoncrawl-examples.git	 has travis:False
example-babel2012: https://github.com/commoncrawl/example-babel2012.git	 has travis:False
example-europeanjob: https://github.com/commoncrawl/example-europeanjob.git	 has travis:False
example-languageentropy: https://github.com/commoncrawl/example-languageentropy.git	 has travis:False
example-apprankings: https://github.com/commoncrawl/example-apprankings.git	 has travis:False
example-javascriptusage: https://github.com/commoncrawl/example-javascriptusage.git	 has travis:False
example-companyfootprints: https://github.com/commoncrawl/example-companyfootprints.git	 has travis:False
example-wikientities: https://github.com/commoncrawl/example-wikientities.git	 has travis:False
example-warc-java: https://github.com/commoncrawl/example-warc-java.git	 has travis:False
nutch: https://github.com/commoncrawl/nutch.git	 has travis:False
  total repos for apache: 30
tapestry3: https://github.com/apache/tapestry3.git	 has travis:False
james: https://github.com/apache/james.git	 has travis:False
tapestry4: https://github.com/apache/tapestry4.git	 has travis:False
tapestry5: https://github.com/apache/tapestry5.git	 has travis:False
sling: https://github.com/apache/sling.git	 has travis:True
xalan-j: https://github.com/apache/xalan-j.git	 has travis:False
zookeeper: https://github.com/apache/zookeeper.git	 has travis:False
tomcat60: https://github.com/apache/tomcat60.git	 has travis:False
jspwiki: https://github.com/apache/jspwiki.git	 has travis:False
ofbiz: https://github.com/apache/ofbiz.git	 has travis:False
directory-studio: https://github.com/apache/directory-studio.git	 has travis:False
felix: https://github.com/apache/felix.git	 has travis:False
chainsaw: https://github.com/apache/chainsaw.git	 has travis:False
maven-wagon: https://github.com/apache/maven-wagon.git	 has travis:False
maven-resources: https://github.com/apache/maven-resources.git	 has travis:False
rat: https://github.com/apache/rat.git	 has travis:False
struts-maven: https://github.com/apache/struts-maven.git	 has travis:False
camel: https://github.com/apache/camel.git	 has travis:False
fop: https://github.com/apache/fop.git	 has travis:False
maven-scm: https://github.com/apache/maven-scm.git	 has travis:False
Total repos for Java: 79
Total repos with Travis: 18