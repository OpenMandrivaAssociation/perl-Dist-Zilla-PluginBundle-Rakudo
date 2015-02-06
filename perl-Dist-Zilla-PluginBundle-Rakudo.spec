%define upstream_name    Dist-Zilla-PluginBundle-Rakudo
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Rakudo bundle for dist-zilla
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Plugin::AutoVersion)
BuildRequires:	perl(Dist::Zilla::Plugin::GatherDir)
BuildRequires:	perl(Dist::Zilla::Plugin::GitObtain)
BuildRequires:	perl(Dist::Zilla::Plugin::License)
BuildRequires:	perl(Dist::Zilla::Plugin::Manifest)
BuildRequires:	perl(Dist::Zilla::Plugin::PruneCruft)
BuildRequires:	perl(Dist::Zilla::Plugin::PruneFiles)
BuildRequires:	perl(Dist::Zilla::Plugin::SvnObtain)
BuildRequires:	perl(Dist::Zilla::Plugin::TemplateFiles)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Git)
BuildArch:	noarch

%description
Rakudo bundle for dist-zilla.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

