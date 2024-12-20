# Configuration Script for E-commerce Collections Schema
# This script defines the schema for each collection, including field descriptions.
# It can be used by an AI agent for data processing and analysis.

collections = {
    "customers": {
        "description": "Stores detailed customer information, including personal details, contact information, preferences, and demographic data.",
        "fields": {
            "_id": {
                "type": "ObjectId",
                "description": "MongoDB's unique identifier"
            },
            "customerId": {
                "type": "NumberInt",
                "description": "Unique identifier for the customer, from customer_customers.customerid"
            },
            "customerCode": {
                "type": "String",
                "description": "Customer code, from customer_customers.customercode"
            },
            "title": {
                "type": "String",
                "description": "Title of the customer (e.g., Mr., Ms.), from customer_customers.title"
            },
            "firstName": {
                "type": "String",
                "description": "First name of the customer, from customer_customers.firstname"
            },
            "middleName": {
                "type": "String",
                "description": "Middle name of the customer, from customer_customers.middlename"
            },
            "lastName": {
                "type": "String",
                "description": "Last name of the customer, from customer_customers.lastname"
            },
            "suffix": {
                "type": "String",
                "description": "Suffix of the customer's name (e.g., Jr., Sr.), from customer_customers.suffix"
            },
            "gender": {
                "type": "String",
                "description": "Gender of the customer, from customer_customerdetails.gender"
            },
            "dateOfBirth": {
                "type": "ISODate",
                "description": "Date of birth of the customer, from customer_customerdetails.dateofbirth"
            },
            "ageGroup": {
                "type": "Embedded Document",
                "description": "Age group information of the customer",
                "fields": {
                    "ageGroupId": {
                        "type": "NumberInt",
                        "description": "Age group ID, from customer_customerdetails.agegroupid"
                    },
                    "ageGroupName": {
                        "type": "String",
                        "description": "Name of the age group, from customer_mstagegroup.agegroupname"
                    }
                }
            },
            "email": {
                "type": "String",
                "description": "Primary email address of the customer, from customer_customers.emailid"
            },
            "alternateEmail": {
                "type": "String",
                "description": "Alternate email address, from customer_customerdetails.alternateemail"
            },
            "phoneNumbers": {
                "type": "Embedded Document",
                "description": "Contact phone numbers of the customer",
                "fields": {
                    "home": {
                        "type": "String",
                        "description": "Home phone number, from customer_customers.homephone"
                    },
                    "mobile": {
                        "type": "String",
                        "description": "Mobile phone number, from customer_customers.mobilephone"
                    },
                    "work": {
                        "type": "String",
                        "description": "Work phone number, from customer_customerdetails.workphone"
                    },
                    "fax": {
                        "type": "String",
                        "description": "Fax number, from customer_customerdetails.faxnumber"
                    }
                }
            },
            "addresses": {
                "type": "Array",
                "description": "List of addresses associated with the customer",
                "items": {
                    "type": "Embedded Document",
                    "fields": {
                        "addressId": {
                            "type": "NumberInt",
                            "description": "Unique identifier for the address, from customer_addresses.addressid"
                        },
                        "addressType": {
                            "type": "String",
                            "description": "Type of address (e.g., Home, Work), from customer_mstaddresstypes.name"
                        },
                        "isDefault": {
                            "type": "Boolean",
                            "description": "Indicates if this is the default address, from customer_addresses.isdefaultaddress"
                        },
                        "forename": {
                            "type": "String",
                            "description": "First name associated with the address, from customer_addresses.forename"
                        },
                        "surname": {
                            "type": "String",
                            "description": "Last name associated with the address, from customer_addresses.surname"
                        },
                        "company": {
                            "type": "String",
                            "description": "Company name, from customer_addresses.companyname"
                        },
                        "street": {
                            "type": "String",
                            "description": "Street address, from customer_addresses.address1"
                        },
                        "address2": {
                            "type": "String",
                            "description": "Additional address information, from customer_addresses.address2"
                        },
                        "city": {
                            "type": "String",
                            "description": "City, from customer_addresses.town"
                        },
                        "state": {
                            "type": "String",
                            "description": "State or province, mapped from customer_addresses.stateid to system_mststates.statename"
                        },
                        "postalCode": {
                            "type": "String",
                            "description": "Postal or ZIP code, from customer_addresses.postcode"
                        },
                        "country": {
                            "type": "String",
                            "description": "Country, from customer_mstcountry.countryname"
                        },
                        "phoneNumber": {
                            "type": "String",
                            "description": "Phone number associated with the address, from customer_addresses.phonenumber"
                        },
                        "isBillingAddress": {
                            "type": "Boolean",
                            "description": "Indicates if this is the billing address"
                        },
                        "isShippingAddress": {
                            "type": "Boolean",
                            "description": "Indicates if this is the shipping address"
                        }
                    }
                }
            },
            "preferences": {
                "type": "Embedded Document",
                "description": "Customer's communication and language preferences",
                "fields": {
                    "receiveOffersByEmail": {
                        "type": "Boolean",
                        "description": "Opt-in for receiving offers via email, from customer_customerdetails.isreceiveofferbyemail"
                    },
                    "receiveOffersBySMS": {
                        "type": "Boolean",
                        "description": "Opt-in for receiving offers via SMS, from customer_customerdetails.isreceiveofferbysms"
                    },
                    "receiveOffersByMail": {
                        "type": "Boolean",
                        "description": "Opt-in for receiving offers via mail, from customer_customerdetails.isreceiveofferbymail"
                    },
                    "preferredContactMethod": {
                        "type": "String",
                        "description": "Preferred method of contact, from customer_customerdetails.preferredcontactmethod"
                    },
                    "preferredShippingMethod": {
                        "type": "String",
                        "description": "Preferred shipping method, from customer_customerdetails.preferredshippingmethod"
                    },
                    "preferredLanguage": {
                        "type": "String",
                        "description": "Preferred language, from customer_customerdetails.preferredlanguage"
                    }
                }
            },
            "status": {
                "type": "Embedded Document",
                "description": "Status information of the customer",
                "fields": {
                    "statusId": {
                        "type": "NumberInt",
                        "description": "Status ID, from customer_customers.statusid"
                    },
                    "statusName": {
                        "type": "String",
                        "description": "Name of the status, from system_mststatus.name"
                    }
                }
            },
            "customerType": {
                "type": "String",
                "description": "Type of customer (e.g., Retail, Wholesale), mapped from customer_customers.customertypeid to customer_mstcustomertypes.name"
            },
            "loyaltyPoints": {
                "type": "NumberInt",
                "description": "Accumulated loyalty points, from customer_customerdetails.loyaltypoints"
            },
            "loyaltyTier": {
                "type": "String",
                "description": "Loyalty tier level, derived from loyaltyPoints or loyalty program data"
            },
            "totalLifetimeValue": {
                "type": "NumberDecimal",
                "description": "Total value of purchases made by the customer, calculated from sales data"
            },
            "registrationSource": {
                "type": "String",
                "description": "Source through which the customer registered, from customer_customerdetails.registrationsource"
            },
            "referralCode": {
                "type": "String",
                "description": "Referral code used during registration, from customer_customerdetails.referralcode"
            },
            "createdDate": {
                "type": "ISODate",
                "description": "Date when the customer record was created, from customer_customers.createddate"
            },
            "lastUpdated": {
                "type": "ISODate",
                "description": "Date when the customer record was last updated, from customer_customers.updateddate"
            },
            "lastLoggedIn": {
                "type": "ISODate",
                "description": "Date when the customer last logged in, from customer_customerdetails.lastloggedin"
            },
            "notes": {
                "type": "String",
                "description": "Additional notes about the customer, from customer_customerdetails.customernotes"
            },
            "orderIds": {
                "type": "Array of NumberInt",
                "description": "List of order IDs associated with the customer, from sales_salesorders.customerid"
            },
            "marketingSegment": {
                "type": "String",
                "description": "Marketing segment the customer belongs to, derived based on analysis"
            },
            "occupation": {
                "type": "String",
                "description": "Customer's occupation, from customer_customerdetails.occupation"
            },
            "maritalStatus": {
                "type": "String",
                "description": "Marital status of the customer, from customer_customerdetails.maritalstatus"
            },
            "numberOfDependents": {
                "type": "NumberInt",
                "description": "Number of dependents, from customer_customerdetails.numberofdependents"
            },
            "annualIncome": {
                "type": "NumberDecimal",
                "description": "Annual income of the customer, from customer_customerdetails.annualincome"
            },
            "educationLevel": {
                "type": "String",
                "description": "Education level of the customer, from customer_customerdetails.educationlevel"
            },
            "socialMediaProfiles": {
                "type": "Embedded Document",
                "description": "Customer's social media profile links",
                "fields": {
                    "facebook": {
                        "type": "String",
                        "description": "Facebook profile link, from customer_customerdetails.facebookprofile"
                    },
                    "twitter": {
                        "type": "String",
                        "description": "Twitter handle, from customer_customerdetails.twitterhandle"
                    },
                    "linkedin": {
                        "type": "String",
                        "description": "LinkedIn profile link, from customer_customerdetails.linkedinprofile"
                    }
                }
            }
        }
    },

    "orders": {
        "description": "Stores comprehensive order details, including payment information, shipping details, and order line items.",
        "fields": {
            "_id": {
                "type": "ObjectId",
                "description": "MongoDB's unique identifier"
            },
            "salesorderid": {
                "type": "NumberInt",
                "description": "Unique identifier for the order, from sales_salesorders.salesorderid"
            },
            "orderCode": {
                "type": "String",
                "description": "Order code, from sales_salesorders.salesordercode"
            },
            "orderDate": {
                "type": "ISODate",
                "description": "Date when the order was placed, from sales_salesorders.orderdate"
            },
            "orderTime": {
                "type": "String",
                "description": "Time when the order was placed, from sales_salesorders.ordertime"
            },
            "customerId": {
                "type": "NumberInt",
                "description": "Identifier of the customer who placed the order, from sales_salesorders.customerid"
            },
            "customer": {
                "type": "Embedded Document",
                "description": "Basic customer information for quick reference",
                "fields": {
                    "customerCode": {
                        "type": "String",
                        "description": "Customer code, from customer_customers.customercode"
                    },
                    "firstName": {
                        "type": "String",
                        "description": "First name of the customer, from customer_customers.firstname"
                    },
                    "lastName": {
                        "type": "String",
                        "description": "Last name of the customer, from customer_customers.lastname"
                    },
                    "email": {
                        "type": "String",
                        "description": "Email of the customer, from customer_customers.emailid"
                    }
                }
            },
            "departmentId": {
                "type": "NumberInt",
                "description": "Department associated with the order, from sales_salesorders.departmentid"
            },
            "salesChannel": {
                "type": "Embedded Document",
                "description": "Information about the sales channel through which the order was placed",
                "fields": {
                    "channelId": {
                        "type": "NumberInt",
                        "description": "Sales channel ID, from sales_mstsaleschannels.saleschannelid"
                    },
                    "channelCode": {
                        "type": "String",
                        "description": "Code of the sales channel, from sales_mstsaleschannels.code"
                    },
                    "channelName": {
                        "type": "String",
                        "description": "Name of the sales channel, from sales_mstsaleschannels.name"
                    }
                }
            },
            "status": {
                "type": "String",
                "description": "Current status of the order, from sales_salesorders.status_name"
            },
            "payment": {
                "type": "Embedded Document",
                "description": "Payment information for the order",
                "fields": {
                    "paymentMethod": {
                        "type": "String",
                        "description": "Payment method used, mapped from sales_salesorders.paymentgatewayid"
                    },
                    "paymentStatus": {
                        "type": "String",
                        "description": "Status of the payment, derived from sales_salesorders.ispaymentreceived"
                    },
                    "transactionId": {
                        "type": "String",
                        "description": "Transaction ID from the payment gateway, from sales_salesorders.transactionid"
                    },
                    "paymentDate": {
                        "type": "ISODate",
                        "description": "Date when the payment was processed, from sales_salesorders.paymentdate"
                    }
                }
            },
            "shipping": {
                "type": "Embedded Document",
                "description": "Shipping information for the order",
                "fields": {
                    "shippingMethod": {
                        "type": "String",
                        "description": "Shipping method used, mapped from sales_salesorders.shippingmethodid"
                    },
                    "shippingAddress": {
                        "type": "Embedded Document",
                        "description": "Shipping address details",
                        "fields": {
                            "addressId": {
                                "type": "NumberInt",
                                "description": "Address ID, from sales_salesorders.shippingaddressid or customer_addresses.addressid"
                            },
                            "addressType": {
                                "type": "String",
                                "description": "Type of address"
                            },
                            "street": {
                                "type": "String",
                                "description": "Street address"
                            },
                            "address2": {
                                "type": "String",
                                "description": "Additional address information"
                            },
                            "city": {
                                "type": "String",
                                "description": "City"
                            },
                            "state": {
                                "type": "String",
                                "description": "State or province"
                            },
                            "postalCode": {
                                "type": "String",
                                "description": "Postal or ZIP code"
                            },
                            "country": {
                                "type": "String",
                                "description": "Country"
                            },
                            "phoneNumber": {
                                "type": "String",
                                "description": "Phone number associated with the address"
                            }
                        }
                    },
                    "billingAddress": {
                        "type": "Embedded Document",
                        "description": "Billing address details",
                        "fields": {
                            "addressId": {
                                "type": "NumberInt",
                                "description": "Address ID, from sales_salesorders.billingaddressid or customer_addresses.addressid"
                            },
                            "addressType": {
                                "type": "String",
                                "description": "Type of address"
                            },
                            "street": {
                                "type": "String",
                                "description": "Street address"
                            },
                            "address2": {
                                "type": "String",
                                "description": "Additional address information"
                            },
                            "city": {
                                "type": "String",
                                "description": "City"
                            },
                            "state": {
                                "type": "String",
                                "description": "State or province"
                            },
                            "postalCode": {
                                "type": "String",
                                "description": "Postal or ZIP code"
                            },
                            "country": {
                                "type": "String",
                                "description": "Country"
                            },
                            "phoneNumber": {
                                "type": "String",
                                "description": "Phone number associated with the address"
                            }
                        }
                    },
                    "shippingCharges": {
                        "type": "NumberDecimal",
                        "description": "Shipping charges for the order, from sales_salesorders.shippingcharges"
                    },
                    "trackingNumber": {
                        "type": "String",
                        "description": "Tracking number for shipment, from sales_salesorders.trackingnumber"
                    },
                    "estimatedDeliveryDate": {
                        "type": "ISODate",
                        "description": "Estimated delivery date, from sales_salesorders.customeredd"
                    },
                    "actualDeliveryDate": {
                        "type": "ISODate",
                        "description": "Actual delivery date, from sales_salesorders.deliverydate"
                    }
                }
            },
            "totalAmounts": {
                "type": "Embedded Document",
                "description": "Monetary amounts related to the order",
                "fields": {
                    "grossAmount": {
                        "type": "NumberDecimal",
                        "description": "Total gross amount, from sales_salesorders.totalgrossamount"
                    },
                    "netAmount": {
                        "type": "NumberDecimal",
                        "description": "Total net amount, from sales_salesorders.totalnetamount"
                    },
                    "vatAmount": {
                        "type": "NumberDecimal",
                        "description": "Total VAT amount, from sales_salesorders.totalvatamt"
                    },
                    "discountAmount": {
                        "type": "NumberDecimal",
                        "description": "Total discount amount, from sales_salesorders.totaldiscountamt"
                    },
                    "shippingCharges": {
                        "type": "NumberDecimal",
                        "description": "Shipping charges, from sales_salesorders.shippingcharges"
                    }
                }
            },
            "orderLines": {
                "type": "Array",
                "description": "List of items included in the order",
                "items": {
                    "type": "Embedded Document",
                    "fields": {
                        "salesorderlineid": {
                            "type": "NumberInt",
                            "description": "Order line ID, from sales_salesorderlines.salesorderlineid"
                        },
                        "productId": {
                            "type": "NumberInt",
                            "description": "Product ID, from sales_salesorderlines.productid"
                        },
                        "sku": {
                            "type": "String",
                            "description": "Product SKU, from inventory_products.sku"
                        },
                        "productName": {
                            "type": "String",
                            "description": "Product name, from inventory_products.productname"
                        },
                        "articletypeid": {
                            "type": "NumberInt",
                            "description": "Article type ID, from inventory_products.articletypeid"
                        },
                        "articleTypeName": {
                            "type": "String",
                            "description": "Article type name, from inventory_mstarticletypes.name"
                        },
                        "quantity": {
                            "type": "NumberInt",
                            "description": "Quantity ordered, from sales_salesorderlines.qty"
                        },
                        "price": {
                            "type": "NumberDecimal",
                            "description": "Price per unit, from sales_salesorderlines.price"
                        },
                        "costPrice": {
                            "type": "NumberDecimal",
                            "description": "Cost price of the product, from inventory_products.costprice"
                        },
                        "margin": {
                            "type": "NumberDecimal",
                            "description": "Margin on the product, calculated as price - costPrice"
                        },
                        "discountAmount": {
                            "type": "NumberDecimal",
                            "description": "Discount amount on the product, from sales_salesorderlines.discountamt"
                        },
                        "vatAmount": {
                            "type": "NumberDecimal",
                            "description": "VAT amount for the product, from sales_salesorderlines.vatamount"
                        },
                        "totalNetAmount": {
                            "type": "NumberDecimal",
                            "description": "Total net amount for the line item, from sales_salesorderlines.totalnetamt"
                        },
                        "status": {
                            "type": "String",
                            "description": "Status of the line item, from sales_salesorderlines.status_name"
                        },
                        "departmentId": {
                            "type": "NumberInt",
                            "description": "Department ID associated with the product, from sales_salesorderlines.departmentid"
                        },
                        "warehouseId": {
                            "type": "NumberInt",
                            "description": "Warehouse ID from which the product will be shipped, from sales_salesorderlines.wmswarehouseid"
                        },
                        "serialNumber": {
                            "type": "String",
                            "description": "Serial number of the product, from sales_salesorderlines.serialnumber"
                        },
                        "returnable": {
                            "type": "Boolean",
                            "description": "Indicates if the product is returnable, from sales_salesorderlines.isreturnable"
                        },
                        "giftWrap": {
                            "type": "Boolean",
                            "description": "Indicates if gift wrap was selected, from sales_salesorderlines.isgiftwrap"
                        },
                        "personalization": {
                            "type": "String",
                            "description": "Personalization details, from sales_salesorderlines.personalization"
                        }
                    }
                }
            },
            "discountDetails": {
                "type": "Array",
                "description": "Details of discounts applied to the order",
                "items": {
                    "type": "Embedded Document",
                    "fields": {
                        "discountDetailId": {
                            "type": "NumberInt",
                            "description": "Discount detail ID, from sales_salesorderdiscountdetails.salesorderdiscountdetailid"
                        },
                        "discountId": {
                            "type": "NumberInt",
                            "description": "Discount ID, from sales_salesorderdiscountdetails.discountid"
                        },
                        "discountCode": {
                            "type": "String",
                            "description": "Discount code, mapped from sales_salesorderdiscountdetails.discountcodeid"
                        },
                        "discountType": {
                            "type": "String",
                            "description": "Type of discount, from sales_mstdiscounttypes.name"
                        },
                        "discountAmount": {
                            "type": "NumberDecimal",
                            "description": "Amount of the discount, from sales_salesorderdiscountdetails.discountamt"
                        }
                    }
                }
            },
            "promotionsApplied": {
                "type": "Array of String",
                "description": "List of promotion codes applied to the order, from sales_salesorders.promotioncodes"
            },
            "createdDate": {
                "type": "ISODate",
                "description": "Date when the order was created, from sales_salesorders.createddate"
            },
            "updatedDate": {
                "type": "ISODate",
                "description": "Date when the order was last updated, from sales_salesorders.updateddate"
            },
            "remarks": {
                "type": "String",
                "description": "Additional remarks or notes about the order, from sales_salesorders.remarks"
            },
            "orderSource": {
                "type": "String",
                "description": "Source of the order (e.g., Online, Mobile App), from sales_salesorders.ordersource"
            },
            "affiliateId": {
                "type": "String",
                "description": "Affiliate ID associated with the order, from sales_salesorders.affiliateid"
            },
            "giftMessage": {
                "type": "String",
                "description": "Gift message included with the order, from sales_salesorders.giftmessage"
            }
        }
    },

    "products": {
        "description": "Stores detailed product information, including pricing, inventory data, supplier information, and attributes.",
        "fields": {
            "_id": {
                "type": "ObjectId",
                "description": "MongoDB's unique identifier"
            },
            "productId": {
                "type": "NumberInt",
                "description": "Unique identifier for the product, from inventory_products.productid"
            },
            "sku": {
                "type": "String",
                "description": "Stock Keeping Unit, from inventory_products.sku"
            },
            "productCode": {
                "type": "String",
                "description": "Product code, from inventory_products.productcode"
            },
            "productName": {
                "type": "String",
                "description": "Name of the product, from inventory_products.productname"
            },
            "description": {
                "type": "String",
                "description": "Short description of the product, from inventory_productext.shortdescription"
            },
            "longDescription": {
                "type": "String",
                "description": "Detailed description of the product, from inventory_productext.longdescription"
            },
            "brand": {
                "type": "String",
                "description": "Brand of the product, from inventory_products.brand"
            },
            "vendor": {
                "type": "Embedded Document",
                "description": "Vendor information",
                "fields": {
                    "vendorId": {
                        "type": "NumberInt",
                        "description": "Vendor ID, from inventory_products.vendorid"
                    },
                    "vendorName": {
                        "type": "String",
                        "description": "Name of the vendor, from inventory_vendors.name"
                    }
                }
            },
            "manufacturer": {
                "type": "Embedded Document",
                "description": "Manufacturer information",
                "fields": {
                    "manufacturerId": {
                        "type": "NumberInt",
                        "description": "Manufacturer ID, from inventory_products.manufacturerid"
                    },
                    "manufacturerName": {
                        "type": "String",
                        "description": "Name of the manufacturer, from inventory_manufacturers.name"
                    }
                }
            },
            "category": {
                "type": "Embedded Document",
                "description": "Category information",
                "fields": {
                    "categoryId": {
                        "type": "NumberInt",
                        "description": "Category ID, from inventory_category.categoryid"
                    },
                    "categoryName": {
                        "type": "String",
                        "description": "Name of the category, from inventory_category.name"
                    }
                }
            },
            "subCategory": {
                "type": "Embedded Document",
                "description": "Subcategory information",
                "fields": {
                    "subCategoryId": {
                        "type": "NumberInt",
                        "description": "Subcategory ID, from inventory_subcategory.subcategoryid"
                    },
                    "subCategoryName": {
                        "type": "String",
                        "description": "Name of the subcategory, from inventory_subcategory.name"
                    }
                }
            },
            "articletypeid": {
                "type": "NumberInt",
                "description": "Article type ID, from inventory_products.articletypeid"
            },
            "articleTypeName": {
                "type": "String",
                "description": "Article type name, from inventory_mstarticletypes.name"
            },
            "attributes": {
                "type": "Embedded Document",
                "description": "Product attributes and specifications",
                "fields": {
                    "color": {
                        "type": "String",
                        "description": "Color of the product, from inventory_productattributes.color"
                    },
                    "size": {
                        "type": "String",
                        "description": "Size of the product, from inventory_productattributes.size"
                    },
                    "weight": {
                        "type": "NumberDecimal",
                        "description": "Weight of the product, from inventory_products.productweight"
                    },
                    "dimensions": {
                        "type": "String",
                        "description": "Dimensions of the product, from inventory_productattributes.dimensions"
                    },
                    "material": {
                        "type": "String",
                        "description": "Material of the product, from inventory_productattributes.material"
                    },
                    "stoneCount": {
                        "type": "NumberInt",
                        "description": "Number of stones (for jewelry), from inventory_productext.stonecount"
                    },
                    "diamondCount": {
                        "type": "NumberInt",
                        "description": "Number of diamonds (for jewelry), from inventory_productext.diamondcount"
                    },
                    "origin": {
                        "type": "String",
                        "description": "Country of origin, from inventory_productext.origin"
                    },
                    "warranty": {
                        "type": "String",
                        "description": "Warranty information, from inventory_productattributes.warranty"
                    }
                }
            },
            "inventory": {
                "type": "Embedded Document",
                "description": "Inventory details",
                "fields": {
                    "inventoryType": {
                        "type": "String",
                        "description": "Type of inventory management, mapped from inventory_products.inventorytypeid"
                    },
                    "quantityAvailable": {
                        "type": "NumberInt",
                        "description": "Available stock quantity, from stock_current.stockqty"
                    },
                    "quantityReserved": {
                        "type": "NumberInt",
                        "description": "Reserved stock quantity, from stock_reserved.reservedqty"
                    },
                    "reorderLevel": {
                        "type": "NumberInt",
                        "description": "Reorder level threshold, from inventory_products.reorderlevel"
                    },
                    "warehouseLocations": {
                        "type": "Array",
                        "description": "List of warehouse locations where the product is stored",
                        "items": {
                            "type": "Embedded Document",
                            "fields": {
                                "warehouseId": {
                                    "type": "NumberInt",
                                    "description": "Warehouse ID, from stock_warehouselocations.warehouseid"
                                },
                                "warehouseName": {
                                    "type": "String",
                                    "description": "Name of the warehouse, from system_mstwarehouses.name"
                                },
                                "quantity": {
                                    "type": "NumberInt",
                                    "description": "Quantity in the warehouse, from stock_warehouselocations.quantity"
                                }
                            }
                        }
                    }
                }
            },
            "price": {
                "type": "Embedded Document",
                "description": "Pricing details",
                "fields": {
                    "costPrice": {
                        "type": "NumberDecimal",
                        "description": "Cost price of the product, from inventory_products.costprice"
                    },
                    "retailPrice": {
                        "type": "NumberDecimal",
                        "description": "Retail price of the product, from inventory_products.highprice"
                    },
                    "webPrice": {
                        "type": "NumberDecimal",
                        "description": "Online price of the product, from inventory_products.webprice"
                    },
                    "clearancePrice": {
                        "type": "NumberDecimal",
                        "description": "Clearance price, from inventory_products.clearanceprice"
                    },
                    "discountPrice": {
                        "type": "NumberDecimal",
                        "description": "Discounted price, from inventory_products.discountprice"
                    },
                    "currency": {
                        "type": "String",
                        "description": "Currency code, from inventory_products.currencycode"
                    }
                }
            },
            "tax": {
                "type": "Embedded Document",
                "description": "Tax information",
                "fields": {
                    "isVatable": {
                        "type": "Boolean",
                        "description": "Indicates if the product is subject to VAT, from inventory_products.isvatincluded"
                    },
                    "vatRate": {
                        "type": "NumberDecimal",
                        "description": "Applicable VAT rate, from inventory_products.vatrate"
                    }
                }
            },
            "images": {
                "type": "Array",
                "description": "List of product images",
                "items": {
                    "type": "Embedded Document",
                    "fields": {
                        "imageUrl": {
                            "type": "String",
                            "description": "URL of the image, from inventory_productimages.imagename"
                        },
                        "altText": {
                            "type": "String",
                            "description": "Alternative text for the image, from inventory_productimages.description"
                        },
                        "isPrimary": {
                            "type": "Boolean",
                            "description": "Indicates if this is the primary image, from inventory_productimages.isprimary"
                        }
                    }
                }
            },
            "status": {
                "type": "Embedded Document",
                "description": "Status flags for the product",
                "fields": {
                    "isActive": {
                        "type": "Boolean",
                        "description": "Indicates if the product is active, from inventory_products.isactive"
                    },
                    "isPromotional": {
                        "type": "Boolean",
                        "description": "Indicates if the product is on promotion, from inventory_products.ispromotional"
                    },
                    "isDiscontinued": {
                        "type": "Boolean",
                        "description": "Indicates if the product is discontinued, from inventory_products.isdiscontinued"
                    }
                }
            },
            "ratings": {
                "type": "Embedded Document",
                "description": "Customer ratings and reviews for the product",
                "fields": {
                    "averageRating": {
                        "type": "NumberDecimal",
                        "description": "Average rating, calculated from customer_reviews.rating"
                    },
                    "reviewCount": {
                        "type": "NumberInt",
                        "description": "Number of reviews, count of customer_reviews for this product"
                    }
                }
            },
            "relatedProducts": {
                "type": "Array of NumberInt",
                "description": "List of related product IDs, from inventory_relatedproducts.relatedproductid"
            },
            "createdDate": {
                "type": "ISODate",
                "description": "Date when the product was created, from inventory_products.createddate"
            },
            "lastUpdated": {
                "type": "ISODate",
                "description": "Date when the product was last updated, from inventory_products.updateddate"
            }
        }
    },

    "departments": {
        "description": "Stores detailed department information, including hierarchy and additional attributes.",
        "fields": {
            "_id": {
                "type": "ObjectId",
                "description": "MongoDB's unique identifier"
            },
            "departmentId": {
                "type": "NumberInt",
                "description": "Unique identifier for the department, from system_mstdepartments.departmentid"
            },
            "departmentCode": {
                "type": "String",
                "description": "Code of the department, from system_mstdepartments.code"
            },
            "departmentName": {
                "type": "String",
                "description": "Name of the department, from system_mstdepartments.name"
            },
            "description": {
                "type": "String",
                "description": "Description of the department, from system_mstdepartments.description"
            },
            "parentDepartmentId": {
                "type": "NumberInt",
                "description": "ID of the parent department (if applicable), from system_mstdepartments.parentid"
            },
            "departmentLevel": {
                "type": "NumberInt",
                "description": "Level of the department in the hierarchy, calculated or from system_mstdepartments.level"
            },
            "isActive": {
                "type": "Boolean",
                "description": "Indicates if the department is active, from system_mstdepartments.isactive"
            },
            "isSalesOrder": {
                "type": "Boolean",
                "description": "Indicates if the department handles sales orders, from system_mstdepartments.issalesorder"
            },
            "managerId": {
                "type": "NumberInt",
                "description": "ID of the department manager, from system_mstdepartments.managerid"
            },
            "createdDate": {
                "type": "ISODate",
                "description": "Date when the department was created, from system_mstdepartments.createddate"
            },
            "lastUpdated": {
                "type": "ISODate",
                "description": "Date when the department was last updated, from system_mstdepartments.auditdate"
            }
        }
    },

    "marketingData": {
        "description": "Stores comprehensive marketing and campaign data, including detailed metrics and attributes for analysis.",
        "fields": {
            "_id": {
                "type": "ObjectId",
                "description": "MongoDB's unique identifier"
            },
            "date": {
                "type": "ISODate",
                "description": "Date of the marketing data, from northbeam_data.date"
            },
            "platform": {
                "type": "String",
                "description": "Marketing platform (e.g., Google, Facebook), from northbeam_data.breakdown_platform_northbeam"
            },
            "campaignName": {
                "type": "String",
                "description": "Name of the marketing campaign, from northbeam_campaign_data.campaign_name"
            },
            "campaignId": {
                "type": "String",
                "description": "ID of the marketing campaign, from northbeam_campaign_data.campaign_id"
            },
            "adGroup": {
                "type": "String",
                "description": "Ad group name or identifier, from northbeam_data.ad_group"
            },
            "adId": {
                "type": "String",
                "description": "Ad identifier, from northbeam_data.ad_id"
            },
            "creative": {
                "type": "String",
                "description": "Description or ID of the ad creative, from northbeam_data.creative"
            },
            "metrics": {
                "type": "Embedded Document",
                "description": "Performance metrics of the marketing data",
                "fields": {
                    "impressions": {
                        "type": "NumberInt",
                        "description": "Number of times the ad was displayed, from northbeam_data.imprs"
                    },
                    "clicks": {
                        "type": "NumberInt",
                        "description": "Number of clicks on the ad, from northbeam_data.clicks"
                    },
                    "spend": {
                        "type": "NumberDecimal",
                        "description": "Amount spent on the ad, from northbeam_data.spend"
                    },
                    "transactions": {
                        "type": "NumberInt",
                        "description": "Number of transactions attributed to the ad, from northbeam_data.transactions"
                    },
                    "transactions1stTime": {
                        "type": "NumberInt",
                        "description": "Number of first-time transactions, from northbeam_data.transactions_1st_time"
                    },
                    "transactionsReturning": {
                        "type": "NumberInt",
                        "description": "Number of returning customer transactions, from northbeam_data.transactions_returning"
                    },
                    "revenue": {
                        "type": "NumberDecimal",
                        "description": "Revenue attributed to the ad, from northbeam_data.attributed_rev"
                    },
                    "roas": {
                        "type": "NumberDecimal",
                        "description": "Return on ad spend, from northbeam_data.roas"
                    },
                    "cac": {
                        "type": "NumberDecimal",
                        "description": "Customer acquisition cost, from northbeam_data.cac"
                    },
                    "ctr": {
                        "type": "NumberDecimal",
                        "description": "Click-through rate, from northbeam_data.ctr"
                    },
                    "cpc": {
                        "type": "NumberDecimal",
                        "description": "Cost per click, from northbeam_data.cpc"
                    },
                    "cpm": {
                        "type": "NumberDecimal",
                        "description": "Cost per thousand impressions, from northbeam_data.cpm"
                    },
                    "newVisits": {
                        "type": "NumberInt",
                        "description": "Number of new visits, from northbeam_data.new_visits"
                    },
                    "percentNewVisits": {
                        "type": "NumberDecimal",
                        "description": "Percentage of new visits, from northbeam_data.percent_new_visits"
                    },
                    "ecr": {
                        "type": "NumberDecimal",
                        "description": "E-commerce conversion rate, from northbeam_data.ecr"
                    },
                    "bounceRate": {
                        "type": "NumberDecimal",
                        "description": "Bounce rate of the ad, from northbeam_data.bounce_rate"
                    }
                }
            },
            "attribution": {
                "type": "Embedded Document",
                "description": "Attribution model information",
                "fields": {
                    "model": {
                        "type": "String",
                        "description": "Attribution model used, from northbeam_data.attribution_model"
                    },
                    "window": {
                        "type": "String",
                        "description": "Attribution window, from northbeam_data.attribution_window"
                    }
                }
            },
            "targetAudience": {
                "type": "String",
                "description": "Description of the target audience, from northbeam_data.target_audience"
            },
            "deviceType": {
                "type": "String",
                "description": "Type of device used (e.g., Desktop, Mobile), from northbeam_data.device_type"
            },
            "geography": {
                "type": "String",
                "description": "Geographic targeting information, from northbeam_data.geography"
            },
            "accountingMode": {
                "type": "String",
                "description": "Accounting mode used, from northbeam_data.accounting_mode"
            },
            "createdDate": {
                "type": "ISODate",
                "description": "Date when the record was created or loaded"
            }
        }
    }

}
