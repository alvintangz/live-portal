from import_export import resources, fields, widgets
from .models import CorporateIndividual, CorporateOrganization

class CorporateOrganizationResource(resources.ModelResource):
    
    id = fields.Field(attribute="id")

    name = fields.Field(attribute="name",
        column_name="Name of Organization - Req.")

    partner = fields.Field(attribute="partner - Req.",
        widget=widgets.BooleanWidget(),
        column_name="Is Partner")
    
    partner_type = fields.Field(attribute="partner_type",
        column_name="Partner Type")

    class Meta:
        fields = ('id',
            'name',
            'partner',
            'partner_type')
        skip_unchanged = True
        model = CorporateOrganization

class CorporateIndividualResource(resources.ModelResource):
    
    id = fields.Field(attribute="id")

    type_of = fields.Field(attribute="type_of",
        column_name="Type - Req.")
    
    organization = fields.Field(attribute="organization",
        widget=widgets.ForeignKeyWidget(CorporateOrganization, 'name'),
        column_name="Organization - Req.")
    
    position_org = fields.Field(attribute="position_org",
        column_name="Position - Req.")

    full_name = fields.Field(attribute="full_name",
        column_name="Full Name - Req.")

    email = fields.Field(attribute="email",
        column_name="Email Address")

    linkedin = fields.Field(attribute="linkedin",
        column_name="Linkedin (Profile URL)")
    
    biography = fields.Field(attribute="biography",
        column_name="Biography")

    order = fields.Field(attribute="order",
        column_name="Order of Importance - Req.")

    class Meta:
        fields = ('id',
            'type_of',
            'organization',
            'position_org',
            'full_name',
            'email',
            'linkedin',
            'biography',
            'order')
        skip_unchanged = True
        model = CorporateIndividual