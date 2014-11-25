#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	IO
%define		pnam	Cat
%include	/usr/lib/rpm/macros.perl
Summary:	IO::Cat - object-oriented Perl implementation of cat(1)
Summary(pl.UTF-8):	IO::Cat - obiektowa implementacja cat(1) dla Perla
Name:		perl-IO-Cat
Version:	1.01
Release:	11
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6ee423e4b025fd4148c7dafee4d2eec3
URL:		http://search.cpan.org/dist/IO-Cat/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Cat - Object-oriented Perl implementation of cat(1).

%description -l pl.UTF-8
IO::Cat - zorientowana obiektowo implementacja programu cat(1) dla
Perla.

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
%doc Changes
%{perl_vendorlib}/IO/Cat.pm
%{_mandir}/man3/*
