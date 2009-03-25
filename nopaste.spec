
%define realname   App-Nopaste
%define version    0.10
%define release    %mkrel 1

Name:       nopaste
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Http://pastebin.com/
Source:     http://www.cpan.org/modules/by-module/App/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Clipboard)
BuildRequires: perl(Config::INI::Reader)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Git)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Getopt)
BuildRequires: perl(Test::More)
BuildRequires: perl(WWW::Mechanize)

BuildArch: noarch

%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the name
nopaste).

Each pastebin is slightly different. When one pastebin goes down (I'm
looking at you, the http://paste.husk.org manpage), then you have to find a
new one. And if you usually use a script to publish text, then it's too
much hassle.

This module aims to smooth out the differences between pastebins, and
provides redundancy: if one site doesn't work, it just tries a different
one.

%prep
%setup -q -n %{realname}-%{version} 

%build
yes no | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/nopaste
/usr/share/man/man1/nopaste.1.lzma

