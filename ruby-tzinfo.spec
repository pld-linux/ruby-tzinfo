Summary:	DST-aware timezone library
Name:		ruby-tzinfo
Version:	0.3.3
Release:	2
License:	Ruby License
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/tzinfo-%{version}.gem
# Source0-md5:	0b69770c1a791d4b7b0e7e4d4d083399
Source1:	setup.rb
URL:		http://tzinfo.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TZInfo is a library that uses the standard tz (Olson) database to
provide daylight savings aware transformations between times in
different time zones. The tz database is compiled into Ruby classes
which are packaged in the release. No external zoneinfo files are
required at runtime.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
#rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
#rm $RPM_BUILD_ROOT%{ruby_ridir}/created.rid

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/tzinfo.rb
%{ruby_rubylibdir}/tzinfo
