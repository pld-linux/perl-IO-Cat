%include	/usr/lib/rpm/macros.perl
Summary:	IO-Cat perl module
Summary(pl):	Modu³ perla IO-Cat
Name:		perl-IO-Cat
Version:	1.01
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/IO-Cat-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-Cat - Object-oriented Perl implementation of cat(1).

%description -l pl
IO-Cat - zorientowana obiektowo implementacja programu cat(1) dla
perla.

%prep
%setup -q -n IO-Cat-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/IO/Cat.pm
%{_mandir}/man3/*
