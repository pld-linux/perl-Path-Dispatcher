#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Path
%define		pnam	Dispatcher
Summary:	Path::Dispatcher - Flexible and extensible dispatch
Name:		perl-Path-Dispatcher
Version:	1.08
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/ET/ETHER/Path-Dispatcher-%{version}.tar.gz
# Source0-md5:	936f5c08da60f2555d7ed304281e724b
URL:		https://metacpan.org/release/Path-Dispatcher
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Moo
BuildRequires:	perl-MooX-TypeTiny
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl-Type-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
We really like Jifty::Dispatcher and wanted to use it for Prophet's
command line.

The basic operation is that of dispatch. Dispatch takes a path and a
list of rules, and it returns a list of matches. From there you can
"run" the rules that matched. These phases are distinct so that, if
you need to, you can inspect which rules were matched without ever
running their codeblocks.

Tab completion support is also available (see in particular
Path::Dispatcher::Cookbook/How can I configure tab completion for
shells?) for the dispatchers you write.

Each rule may take a variety of different forms (which I think
justifies the "flexible" adjective in the module's description). Some
of the rule types are:

Since Path::Dispatcher is designed with good object-oriented
programming practices, you can also write your own domain-specific
rule classes (which earns it the "extensible" adjective). For example,
in Prophet, we have a custom rule for matching, and tab completing,
record IDs.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Path/*.pm
%{perl_vendorlib}/Path/Dispatcher
%{_mandir}/man3/*
