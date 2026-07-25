%define upstream_name    Dist-Zilla-PluginBundle-Rakudo
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Rakudo bundle for dist-zilla
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Dist-Zilla-PluginBundle-Rakudo
Source0:	https://cpan.metacpan.org/authors/id/D/DU/DUFF/Dist-Zilla-PluginBundle-Rakudo-%{upstream_version}.tar.gz

BuildRequires:	make
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

