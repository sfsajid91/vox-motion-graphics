#!/usr/bin/env python3
from pathlib import Path
import json
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMAS=ROOT/'schemas'

def load(name):
    return json.loads((SCHEMAS/name).read_text())

def assert_valid(schema_name,obj):
    Draft202012Validator(load(schema_name)).validate(obj)

def assert_invalid(schema_name,obj):
    errs=list(Draft202012Validator(load(schema_name)).iter_errors(obj))
    assert errs, f'expected {schema_name} to reject object'

def base_scene():
    return {
      'project': {'aspectRatio':'9:16','fps':30,'targetDurationSec':8},
      'styleProfile': {'name':'clean editorial','palette':['#111111','#eeeeee'],'motionCadence':'tactile then smooth'},
      'scenes':[{
        'id':'S01','beatIds':['B1'],'purpose':'Show a category shift','visualThesis':'Old physical interface is replaced by a software surface',
        'representationType':'metaphor','primaryAction':'Keypad detaches while glass plane takes its footprint','estimatedDurationSec':8,
        'assetRoles':[{'id':'phone','role':'old hardware','preferredSourceStrategy':'programmatic','representationType':'reconstruction'}],
        'qaStatus':'pending_review','visualMechanism':'transformation','launchpad':'glass surface fills frame','constructionFamily':'transformation',
        'microStructure':{'anchor':'phone established','action':'keypad detaches','consequence':'app surface appears','launchpad':'camera enters screen'},
        'attentionContinuity':{'entryZone':'center','exitZone':'center','dominantDirection':'inward','scaleClassIn':'medium','scaleClassOut':'micro','handoffObject':'glass surface','handoffReason':'screen becomes next world'}
      }]
    }

def main():
    # Every schema must itself be structurally valid JSON Schema.
    for p in sorted(SCHEMAS.glob('*.schema.json')):
        Draft202012Validator.check_schema(json.loads(p.read_text()))

    assert_valid('scene-plan.schema.json',base_scene())
    bad=base_scene(); bad['scenes'][0]['qaStatus']='pass'
    assert_invalid('scene-plan.schema.json',bad)

    evidence=base_scene(); evidence['scenes'][0]['representationType']='evidence'; evidence['scenes'][0].pop('claimIds',None)
    assert_invalid('scene-plan.schema.json',evidence)

    asset_plan={
      'projectId':'p','assets':[{
        'id':'historic_phone','role':'literal historical product','usedByScenes':['S1'],'representationType':'literal',
        'strategy':{'preferred':'generate','fallback':'none'},'requirements':{},'motionNeeds':{},
        'provenance':{'rightsStatus':'unresolved'},'approvalStatus':'pending_review'
      }]}
    assert_invalid('asset-plan.schema.json',asset_plan)

    verified={
      'projectId':'p','assets':[{
        'id':'source','role':'source image','usedByScenes':['S1'],'representationType':'literal',
        'strategy':{'preferred':'source','fallback':'reconstruction'},'requirements':{},'motionNeeds':{},
        'provenance':{'rightsStatus':'verified','sourceUri':None,'license':None,'evidence':None},'approvalStatus':'pending_review'
      }]}
    assert_invalid('asset-plan.schema.json',verified)

    ref={
      'referenceId':'ref1','scenes':[{'id':'S1','semanticJob':'reveal','constructionFamily':'portal','visualThesis':'frame becomes world','mechanism':'weld-detach','classification':'technique_recipe'}],
      'findings':[{'finding':'few assets, high choreography','classification':'creator_dna','confidence':'high','evidenceSceneIds':['S1']}]
    }
    assert_valid('reference-analysis.schema.json',ref)

    tune={'projectId':'p','scenes':[{'sceneId':'S1','parameters':[{'name':'heroScale','type':'number','currentValue':1.0,'min':0.5,'max':2.0,'step':0.05,'allowedValues':None,'semanticRole':'focal hierarchy','repairPriority':'high','studioExposed':True}]}]}
    assert_valid('tunable-parameter-manifest.schema.json',tune)

    patch={'critic':'vision-critic','renderId':'r1','changes':[{'sceneId':'S1','parameter':'heroScale','oldValue':1.0,'newValue':1.15,'reason':'hero too weak','expectedEffect':'stronger focal hierarchy','confidence':'high'}],'requiresRedesign':False,'redesignReason':None}
    assert_valid('parameter-patch.schema.json',patch)

    print(f'OK: {len(list(SCHEMAS.glob("*.schema.json")))} schemas + behavioral guardrails')

if __name__=='__main__':
    main()
