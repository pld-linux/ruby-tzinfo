%define pkgname tzinfo
Summary:	DST-aware timezone library
Summary(pl.UTF-8):	Biblioteka stref czasowych uwzględniająca czas letni
Name:		ruby-%{pkgname}
Version:	0.3.16
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	57bb0cbd33c102c5d1a23e3a3c1698fc
URL:		http://tzinfo.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
TZInfo is a library that uses the standard tz (Olson) database to
provide daylight savings aware transformations between times in
different time zones. The tz database is compiled into Ruby classes
which are packaged in the release. No external zoneinfo files are
required at runtime.

%description -l pl.UTF-8
TZInfo to biblioteka wykorzystująca standardową bazę danych tz (Olson)
do udostępniania przekształceń między czasami w różnych strefach
czasowych z uwzględnieniem okresowych zmian czasu (czasu letniego).
Baza danych tz jest wkompilowana w klasy Ruby'ego, które są dołączone
do pakietu. Zewnętrzne pliki zoneinfo nie są potrzebne w czasie
działania.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}

%build
rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/tzinfo.rb
%{ruby_rubylibdir}/tzinfo

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/TZInfo
